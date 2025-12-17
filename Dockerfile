FROM ruby:3.3-bookworm

WORKDIR /srv/jekyll

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    nodejs \
  && rm -rf /var/lib/apt/lists/*

COPY Gemfile Gemfile.lock ./
RUN bundle config set path "/usr/local/bundle" \
  && bundle install

EXPOSE 4000 35729

CMD ["bash", "-lc", "bundle install && bundle exec jekyll serve --config _config.yml,_config.docker.yml --host 0.0.0.0 --livereload --livereload-port 35729 --force_polling --incremental"]
