#!/bin/bash
set -e  # Exit on any error
set -x  # Print commands as they execute

# Set UTF-8 encoding first, before any bundle commands
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export RUBYOPT="-E utf-8"
export LC_CTYPE=en_US.UTF-8
# Prefer rbenv-managed Ruby for Jekyll and Bundler compatibility.
if command -v rbenv >/dev/null 2>&1; then
  export PATH="$HOME/.rbenv/bin:$PATH"
  eval "$(rbenv init -)"
elif [ -d "/opt/homebrew/opt/ruby@3.4/bin" ]; then
  export PATH="/opt/homebrew/opt/ruby@3.4/bin:$PATH"
  export GEM_HOME="$HOME/.gem/ruby/3.4.0"
  export GEM_PATH="/opt/homebrew/opt/ruby@3.4/lib/ruby/gems/3.4.0:$GEM_HOME"
fi
# Ensure locally installed CLI tools (like d2) are on PATH
export PATH="$HOME/.local/bin:$PATH"

# Verify encoding settings
echo "Environment variables:"
echo "LANG=$LANG"
echo "LC_ALL=$LC_ALL"
echo "RUBYOPT=$RUBYOPT"

# Parse args
FAST=0
EXTRA_ARGS=()
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --fast)
      FAST=1
      shift
      ;;
    --help|-h)
      echo "Usage: $0 [--fast]"
      echo "  --fast   Use _config.dev.yml and incremental Jekyll build for a quick build"
      exit 0
      ;;
    *)
      EXTRA_ARGS+=("$1")
      shift
      ;;
  esac
done

if [ "$FAST" -eq 1 ]; then
  echo "Fast build: using _config.dev.yml and incremental Jekyll build"
else
  echo "Normal build"
fi

if ! command -v d2 >/dev/null 2>&1; then
  curl -fsSL https://d2lang.com/install.sh | sh -s --
fi

npm install
npm audit fix --force || true
npm run build

# Test if bundler can read the gemspec
echo "Testing gemspec readability..."
ruby -e "
require 'bundler'
begin
  spec = Bundler.load_gemspec('jekyll-theme-chirpy.gemspec')
  puts 'Gemspec loaded successfully'
  puts \"Files count: #{spec.files.length}\"
rescue => e
  puts \"Error loading gemspec: #{e.message}\"
  puts \"Error class: #{e.class}\"
  exit 1
end
"

bundle install
bundle update

# Build site: use dev config and incremental mode when --fast is passed
if [ "$FAST" -eq 1 ]; then
  JEKYLL_ENV=development bundle exec jekyll build --config _config.yml,_config.dev.yml --incremental
else
  JEKYLL_ENV=production bundle exec jekyll build
fi

# Index site with Pagefind for client-side search (runs after Jekyll completes)
# Continue build even if pagefind fails (fallback: search won't work but site deploys)
npx pagefind --site _site || echo "Warning: Pagefind indexing failed, search may not work"
