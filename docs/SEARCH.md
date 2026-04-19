# Search & Indexing

This document explains how the client-side search works in this blog, which uses Pagefind for full-text indexing and search.

## Overview

- The site uses **Pagefind** for client-side, full-text search. Pagefind indexes the built `_site/` HTML pages and generates a search index and JS module at `_site/pagefind/`.
- Pagefind is run as the final step in `build.sh`, after Jekyll completes. Running `./build.sh` builds and indexes the entire site in one command.
- The search UI is initialized in `_includes/search-loader.html` and reads search results into `#search-results` container.
- The search input, results, and display behavior are managed by `_includes/topbar.html`, `_includes/search-results.html`, and `_javascript/modules/components/search-display.js`.

## How Search Works

1. **Build phase**: When you run `./build.sh`, Jekyll builds the site and then Pagefind indexes it as the final build step:
   - Jekyll compiles Markdown posts and templates to `_site/`
   - `build.sh` runs `npx pagefind --site _site` after Jekyll completes
   - Pagefind crawls all HTML files in `_site/`
   - Extracts text content and metadata (title, excerpt, URL)
   - Generates an index at `_site/pagefind/pagefind.js` and supporting index files
   - Uses `<link rel="canonical">` tags to determine correct page URLs (which handles `baseurl: "/blog"` automatically)

2. **Runtime phase**: When a user types in the search input (`#search-input`):
   - The `search-loader.html` script receives the `input` event
   - It calls `pagefind.search(query)` to search the index
   - Results are rendered as `<article>` elements in `#search-results`
   - The `search-display.js` component shows/hides the results wrapper based on input state

## Key Files

- `build.sh` — runs `npx pagefind --site _site` after Jekyll build completes to generate the search index
- `_includes/search-loader.html` — initializes Pagefind and wires search results to the DOM
- `_includes/search-results.html` — the results wrapper and container (`#search-results`)
- `_includes/topbar.html` — renders the search input (`#search-input`)
- `_includes/js-selector.html` — loads required JS libraries (search.js is no longer loaded)
- `_data/origin/basic.yml` and `cors.yml` — library paths (search.js entry removed)
- `_javascript/modules/components/search-display.js` — handles UI state (show/hide results, mobile search bar)

## Pagefind Configuration

Pagefind is automatically invoked by the Jekyll plugin with default settings. It indexes all HTML files and outputs to `_site/pagefind/`. No additional configuration is needed; Pagefind automatically:

- Extracts text from HTML elements
- Highlights matching terms in excerpts
- Derives page URLs from canonical links (or file paths as fallback)
- Generates a compact search index

## Baseurl Handling

The site has `baseurl: "/blog"` in `_config.yml`, which means:

- Canonical URLs in Jekyll-generated HTML include `/blog/` prefix
- Pagefind reads these canonical URLs and stores `/blog/...` paths in the index
- Search results link to correct paths on the deployed site

## Customization

To modify Pagefind behavior:

1. Edit `build.sh` to add options to the `npx pagefind` command. Examples:
   - `--glob "**/*.html"` — customize which files to index
   - `--output-path _site/custom-pagefind` — change output location (not recommended)
2. Modify the result template in `_includes/search-loader.html` to change how results are displayed (currently shows title and excerpt)
3. Adjust excerpt length or highlight behavior by editing the result rendering logic in `search-loader.html`

## Troubleshooting

- **Search shows no results**: Check that `_site/pagefind/` exists after running `./build.sh`. If not, verify the build output shows pagefind succeeded (look for "Running Pagefind" messages).
- **Results look broken**: Open browser DevTools → Network and check that `/blog/pagefind/pagefind.js` loads without 404. Check that `#search-input` and `#search-results` exist in the DOM.
- **Results have wrong URLs**: Verify that Jekyll is generating `<link rel="canonical">` tags in the HTML (provided by the jekyll-seo-tag gem).
- **Service worker caching**: If you update the search index but see stale results, clear service worker cache (DevTools → Application → Service Workers → Unregister).

## References

- [Pagefind documentation](https://pagefind.app/)
- [Jekyll configuration](https://jekyllrb.com/docs/configuration/)
