from datetime import date as d
import os
from pathlib import Path
import tempfile

def betw(x, a, b)->bool:
    '''Returns True if a <= x <= b'''

    return a <= x <= b

def is_valid_date_format(date)->bool:
    '''Returns True if the date format is valid'''
    date_split = date.split('-')
    if len(date_split)!=3:
        return False

    try:
        year = int(date_split[0])
        month = int(date_split[1])
        day = int(date_split[2])
    except ValueError:
        return False

    return betw(year, 1000, 9999) and betw(month, 1, 12) and betw(day, 1, 31)

def is_valid_tags_format(tags)->bool:
    '''Returns True if the tags format is valid'''
    if not tags:
        return False
    if tags[0] != '[' or tags[-1] != ']':
        return False

    return True 

def parse_input(input):
    '''Changes 'y' or 'n' to boolean values'''
    return True if input == 'y' else False

def parse_post_name(post_name):
    filtered = post_name.replace("-", "")
    split_post_name = filtered.split()
    return "-".join(split_post_name)

def _prompt_yn(prompt: str) -> bool:
    answer = input(prompt).strip().lower()
    while answer not in ("y", "n"):
        answer = input("Please enter either 'y' or 'n'\n").strip().lower()
    return parse_input(answer)

def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
            dir=str(path.parent),
            prefix=f".{path.name}.",
            suffix=".tmp",
        ) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(content)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_path, path)
    finally:
        if tmp_path is not None and tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass

def main() -> int:
    print('Creating a new post template interactively...')
    file_path = ""

    b_date = _prompt_yn("Use today's date? [y/n]\n")
    date = ""

    if b_date:
        date = str(d.today())
    else:
        custom_date = input("Enter date to use in format: yyyy-mm-dd\n").strip()
        while not is_valid_date_format(custom_date):
            custom_date = input(
                "Date was not in the correct format or not valid. Please re-enter in format: yyyy-mm-dd\n"
            ).strip()

        date = custom_date
        print(f"Using custom date: {custom_date}")

    i_post_name = input("Enter a file post name\n").strip()
    while i_post_name == "":
        i_post_name = input("An empty post name is not valid. Please re-enter:\n").strip()
    file_post_name = parse_post_name(i_post_name)

    file_path = str(date) + "-" + str(file_post_name)

    print(f"\nFILE PATH: {file_path}\n")

    content_lines = []
    content_lines.append("---\n")
    content_lines.append("layout: post\n")

    b_post_title = _prompt_yn("Use file post name as post title? [y/n]\n")

    if b_post_title:
        content_lines.append(f"title: {i_post_name}\n")
    else:
        post_title = input("Enter a post title:\n").strip()
        content_lines.append(f"title: {post_title}\n")

    i_subtitle = input("Enter a post subtitle:\n").strip()

    while i_subtitle == "":
        i_subtitle = input("An empty subtitle is not valid. Please re-enter:\n").strip()

    content_lines.append(f"subtitle: {i_subtitle}\n")

    i_tags = input("Enter tags in a pythonic list:\n").strip()

    while not is_valid_tags_format(i_tags):
        i_tags = input("Tags were not of the correct format. Please re-enter:\n").strip()

    content_lines.append(f"tags: {i_tags}\n")

    b_post_type = _prompt_yn("Rigorous post type? [y/n]\n")

    if b_post_type:
        content_lines.append("type: r\n")
    else:
        content_lines.append("type: nr\n")

    content_lines.append("---\n")

    final_path = Path("_posts") / f"{file_path}.md"
    _write_atomic(final_path, "".join(content_lines))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nAborted; no post file created.")
        raise SystemExit(130)
