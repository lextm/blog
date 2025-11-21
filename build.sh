#!/bin/bash
set -e  # Exit on any error
set -x  # Print commands as they execute

echo "=== Debugging Information ==="
echo "Current locale: $(locale)"
echo "Ruby version: $(ruby --version)"
echo "Bundler version: $(bundle --version)"
echo "Git files with potential encoding issues:"
git ls-files | grep -E '[^\x00-\x7F]' || echo "No non-ASCII filenames found"
echo "Files in _data/locales:"
ls -la _data/locales/ 2>/dev/null || echo "_data/locales not found"
echo "================================"

# Set UTF-8 encoding first, before any bundle commands
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export RUBYOPT="-E utf-8"
export LC_CTYPE=en_US.UTF-8

# Verify encoding settings
echo "Environment variables:"
echo "LANG=$LANG"
echo "LC_ALL=$LC_ALL"
echo "RUBYOPT=$RUBYOPT"

# Force UTF-8 for git commands
git config core.quotepath false 2>/dev/null || true

npm install
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

BUNDLE_WITHOUT="development test" bundle install
bundle update
JEKYLL_ENV=production bundle exec jekyll build
