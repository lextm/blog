curl -fsSL https://d2lang.com/install.sh | sh -s --

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
