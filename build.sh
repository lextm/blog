npm install
npm run build

# Set UTF-8 encoding
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export RUBYOPT=-Eutf-8

bundle install
bundle update
JEKYLL_ENV=production bundle exec jekyll build
