curl -fsSL https://d2lang.com/install.sh | sh -s --

npm install
npm run build
bundle update
bundle exec jekyll serve --watch --drafts --host
