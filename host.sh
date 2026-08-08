#!/usr/bin/bash
bundle install
bundle exec jekyll serve --config _config.yml,_config.docker.yml --host 0.0.0.0 --livereload
