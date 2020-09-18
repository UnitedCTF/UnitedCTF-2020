FROM ruby:2.5.7
RUN apt-get update -qq && apt-get install -y sqlite3
RUN mkdir /application
COPY application /application
WORKDIR /application
ENV RAILS_ENV production
ENV BUNDLER_VERSION=2.1.4
ENV RAILS_SERVE_STATIC_FILES=true
ENV FLAG_2=FLAG-94b98c9a4246392468e57df1a85cc649
ENV FLAG_3=FLAG-47e3607c41a277b261556cc39bfe3e38
ENV FLAG_1=FLAG-88541066556eecf7269cf2a4d0220222
ENV SUPPORT_ACCOUNT_NAME="Invoicer Support Account"
ENV SECRET_KEY="39f99671c9d3a697a8f72f876057848dbe47865ea3ccba1bdc1e1bc7b6ece782f9aff2b2ad5e41bb8073a7719d2d16618976b252790d2d4051a6b776a218b4a0"

RUN gem update --system
RUN gem install bundler -v $BUNDLER_VERSION
RUN bundle config --global frozen 1
RUN bundle install
RUN bundle exec rake assets:precompile
RUN bundle exec rake db:create
RUN bundle exec rake db:migrate
RUN bundle exec rake db:seed

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]
