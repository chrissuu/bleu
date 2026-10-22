#!/usr/bin/bash
PORT="${PORT:-4000}"

while lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; do
  PORT=$((PORT + 1))
done

bundle install
bundle exec jekyll serve --config _config.yml,_config.docker.yml --host 0.0.0.0 --port "$PORT" --livereload
