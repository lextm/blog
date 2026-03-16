curl -fsSL https://d2lang.com/install.sh | sh -s --

export PATH="$HOME/.local/bin:$PATH"

npm install
npm run build
bundle update
bundle exec jekyll serve --watch --drafts --host
