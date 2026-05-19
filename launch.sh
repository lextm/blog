curl -fsSL https://d2lang.com/install.sh | sh -s --

# Prefer rbenv-managed Ruby for Jekyll and Bundler compatibility.
if command -v rbenv >/dev/null 2>&1; then
  export PATH="$HOME/.rbenv/bin:$PATH"
  eval "$(rbenv init -)"
elif [ -d "/opt/homebrew/opt/ruby@3.4/bin" ]; then
  export PATH="/opt/homebrew/opt/ruby@3.4/bin:$PATH"
  export GEM_HOME="$HOME/.gem/ruby/3.4.0"
  export GEM_PATH="/opt/homebrew/opt/ruby@3.4/lib/ruby/gems/3.4.0:$GEM_HOME"
fi
export PATH="$HOME/.local/bin:$PATH"

npm install
npm run build
bundle update

# Build initial site and index for search
bundle exec jekyll build --drafts
npx pagefind --site _site

# Start server in watch mode (rebuilds on file changes)
# Note: Run 'npx pagefind --site _site' manually after edits to update search index
bundle exec jekyll serve --watch --drafts --host
