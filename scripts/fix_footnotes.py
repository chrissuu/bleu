#!/usr/bin/env python3
"""Renumber markdown footnotes by in-text appearance order.

The script is occurrence-aware:
- duplicate labels are treated as separate occurrences
- nth reference of a label maps to nth definition block of that label
- duplicate labels are renumbered uniquely (e.g. 1 1 2 -> 1 2 3)
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
DEF_START_RE = re.compile(r"^\[\^([^\]]+)\]:(.*)$")


@dataclass
class DefinitionBlock:
    label: str
    start_line: int
    end_line: int
    lines: List[str]


def collect_reference_occurrences(text: str) -> List[str]:
    order: List[str] = []
    for match in REF_RE.finditer(text):
        order.append(match.group(1))
    return order


def parse_definition_blocks(lines: Sequence[str]) -> List[DefinitionBlock]:
    starts: List[Tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = DEF_START_RE.match(line.rstrip("\n"))
        if m:
            starts.append((i, m.group(1)))

    blocks: List[DefinitionBlock] = []
    for idx, (start_line, label) in enumerate(starts):
        end_line = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        block_lines = list(lines[start_line:end_line])
        blocks.append(
            DefinitionBlock(
                label=label,
                start_line=start_line,
                end_line=end_line,
                lines=block_lines,
            )
        )
    return blocks


def build_occurrence_mapping(
    ref_labels: Sequence[str], def_blocks: Sequence[DefinitionBlock]
) -> Tuple[Dict[int, str], Dict[Tuple[str, int], str], Dict[str, str]]:
    def_indices_by_label: Dict[str, List[int]] = {}
    for idx, block in enumerate(def_blocks):
        def_indices_by_label.setdefault(block.label, []).append(idx)

    # Map each reference occurrence to a definition block index where possible.
    ref_occurrence_to_def_index: Dict[Tuple[str, int], int] = {}
    ref_seen_count: Dict[str, int] = {}
    def_first_ref_pos: Dict[int, int] = {}
    for pos, label in enumerate(ref_labels):
        occ = ref_seen_count.get(label, 0)
        ref_seen_count[label] = occ + 1

        def_indices = def_indices_by_label.get(label, [])
        if not def_indices:
            continue
        chosen = def_indices[occ] if occ < len(def_indices) else def_indices[0]
        ref_occurrence_to_def_index[(label, occ)] = chosen
        if chosen not in def_first_ref_pos:
            def_first_ref_pos[chosen] = pos

    indexed_blocks = list(enumerate(def_blocks))
    sorted_blocks = sorted(
        indexed_blocks,
        key=lambda item: (def_first_ref_pos.get(item[0], sys.maxsize), item[0]),
    )
    block_new_label: Dict[int, str] = {
        idx: str(new_num) for new_num, (idx, _) in enumerate(sorted_blocks, start=1)
    }

    # Fallback numbering for references that have no matching definition blocks.
    fallback_ref_label: Dict[str, str] = {}
    next_label_num = len(def_blocks) + 1
    for label in ref_labels:
        if label in def_indices_by_label:
            continue
        if label not in fallback_ref_label:
            fallback_ref_label[label] = str(next_label_num)
            next_label_num += 1

    ref_occurrence_to_new_label: Dict[Tuple[str, int], str] = {}
    ref_seen_count.clear()
    for label in ref_labels:
        occ = ref_seen_count.get(label, 0)
        ref_seen_count[label] = occ + 1

        mapped_def_idx = ref_occurrence_to_def_index.get((label, occ))
        if mapped_def_idx is not None:
            ref_occurrence_to_new_label[(label, occ)] = block_new_label[mapped_def_idx]
        elif label in def_indices_by_label:
            # More references than definitions: point extra refs at first definition.
            first_def_idx = def_indices_by_label[label][0]
            ref_occurrence_to_new_label[(label, occ)] = block_new_label[first_def_idx]
        else:
            ref_occurrence_to_new_label[(label, occ)] = fallback_ref_label[label]

    return block_new_label, ref_occurrence_to_new_label, fallback_ref_label


def rewrite_references(text: str, ref_occurrence_to_new_label: Dict[Tuple[str, int], str]) -> str:
    seen_counts: Dict[str, int] = {}

    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        occ = seen_counts.get(label, 0)
        seen_counts[label] = occ + 1
        return f"[^{ref_occurrence_to_new_label.get((label, occ), label)}]"

    return REF_RE.sub(repl, text)


def rewrite_definition_header(line: str, new_label: str) -> str:
    line_ending = "\n" if line.endswith("\n") else ""
    stripped = line[:-1] if line_ending else line
    m = DEF_START_RE.match(stripped)
    if not m:
        return line
    suffix = m.group(2)
    return f"[^{new_label}]:{suffix}{line_ending}"


def reorder_and_rewrite_definitions(
    lines: Sequence[str], block_new_label: Dict[int, str]
) -> List[str]:
    blocks = parse_definition_blocks(lines)
    if not blocks:
        return list(lines)
    first_start = blocks[0].start_line
    last_end = blocks[-1].end_line
    sorted_blocks = sorted(blocks, key=lambda b: int(block_new_label.get(def_blocks_index(blocks, b), "0")))

    rewritten_blocks: List[str] = []
    for block in sorted_blocks:
        idx = def_blocks_index(blocks, block)
        new_label = block_new_label.get(idx, block.label)
        new_lines = list(block.lines)
        if new_lines:
            new_lines[0] = rewrite_definition_header(new_lines[0], new_label)
        rewritten_blocks.extend(new_lines)
    return list(lines[:first_start]) + rewritten_blocks + list(lines[last_end:])


def def_blocks_index(blocks: Sequence[DefinitionBlock], target: DefinitionBlock) -> int:
    for idx, block in enumerate(blocks):
        if block.start_line == target.start_line and block.end_line == target.end_line:
            return idx
    return -1


def process_text(text: str) -> str:
    lines = text.splitlines(keepends=True)
    def_blocks = parse_definition_blocks(lines)
    ref_order = collect_reference_occurrences(text)
    if not ref_order and not def_blocks:
        return text

    block_new_label, ref_occ_to_new_label, _ = build_occurrence_mapping(ref_order, def_blocks)

    rewritten_refs = rewrite_references(text, ref_occ_to_new_label)
    rewritten_lines = rewritten_refs.splitlines(keepends=True)
    final_lines = reorder_and_rewrite_definitions(rewritten_lines, block_new_label)
    return "".join(final_lines)


def duplicate_definition_labels(text: str) -> List[str]:
    lines = text.splitlines(keepends=True)
    labels = [b.label for b in parse_definition_blocks(lines)]
    counts: Dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return sorted([label for label, count in counts.items() if count > 1])


def iter_markdown_files(paths: Iterable[Path]) -> List[Path]:
    files: List[Path] = []
    for path in paths:
        if path.is_file():
            files.append(path)
            continue
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
            files.extend(sorted(path.rglob("*.markdown")))
    deduped = sorted(set(files))
    return deduped


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix and renumber markdown footnotes.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["_posts"],
        help="Files or directories to process (default: _posts).",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to files. Without this flag, runs in dry mode.",
    )
    args = parser.parse_args()

    files = iter_markdown_files(Path(p) for p in args.paths)
    if not files:
        print("No markdown files found.")
        return 0

    changed: List[Path] = []
    for file in files:
        original = file.read_text(encoding="utf-8")
        updated = process_text(original)
        if updated != original:
            changed.append(file)
            if args.write:
                file.write_text(updated, encoding="utf-8")

    mode = "Updated" if args.write else "Would update"
    if changed:
        print(f"{mode} {len(changed)} file(s):")
        for path in changed:
            print(path)
    else:
        print("No footnote renumbering changes needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
