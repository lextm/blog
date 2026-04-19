#!/usr/bin/env ruby
#
# Automatically index the site with Pagefind after Jekyll builds

Jekyll::Hooks.register :site, :post_write do |site|
  system('npx pagefind --site _site')
end
