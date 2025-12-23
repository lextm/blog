- When generating a new blog post in this project:

  - Use the correct front matter format: include `layout`, `title`, `description`, `tags`, `categories`, and `excerpt_separator`.
  - Place the new post in the appropriate `_posts/YYYY/` folder, using the filename format `YYYY-MM-DD-title.md` with zero-padded month and day (e.g., `2025-07-26` not `2025-7-26`).
  - Write a long, SEO-friendly summary in the `description` field that clearly explains the post's topic and value.
  - Use relevant tags and categories that already exist in the project. Ask for confirmation before using new tags or categories.
  - Use `<!--more-->` as the excerpt separator after the introductory paragraph.
  - Follow the writing style and structure of previous posts for consistency.
  - When adding backlinks to previous posts, use the correct Jekyll/Liquid link style (e.g., `{% post_url YYYY/MM-DD-title %}`) instead of hardcoded URLs.
  - If the post is a new addition to an existing post series, add a final section inviting readers to visit the tag page for that series to explore related posts. For example, for HttpPlatformHandler-related posts, add a note like: "To explore more on this topic, check out all posts tagged [HttpPlatformHandler]({{ site.baseurl }}/tags/httpplatformhandler/)."
  - Use the correct Liquid syntax for links, e.g., `[link text]({{ site.baseurl }}/path/to/resource/)` instead of hardcoded URLs for tags and categories.
  - Use clean and compact Markdown syntax:

    - Use ATX-style headings (`##` for main heading, `###` for subheadings, etc.) with a space after the hash marks. Do not use single hash (`#`) headings due to Jekyll theme requirements.
    - Ensure proper spacing between paragraphs, headings, and lists (one blank line).
    - Use fenced code blocks with language specifiers (`csharp, `xml, etc.) for better syntax highlighting.
    - Keep line lengths reasonable and use line breaks appropriately for readability in the source.
    - Use reference-style links for cleaner text when there are multiple links to the same source.

  - Header image:

    - Use the nested `image` mapping in post front matter with `path` and `alt` fields to match existing posts. Example:

      ```yaml
      image:
        path: /images/your-image.jpg
        alt: Descriptive alt text for the image
      ```

    - For external images, `path` can be a full URL.
