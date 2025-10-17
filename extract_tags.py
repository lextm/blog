#!/usr/bin/env python3

import os
import re
import yaml
import time

def extract_tags_from_md(file_path):
    """Extract tags from a markdown file's front matter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for YAML front matter between --- markers
        match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
        if not match:
            return []
        
        # Extract the YAML front matter
        front_matter = match.group(1)
        
        # Parse the YAML
        try:
            metadata = yaml.safe_load(front_matter)
            if not metadata or 'tags' not in metadata:
                return []
            
            # Handle different tag formats:
            # 1. tags: tag1 tag2 tag3 (single string with spaces)
            # 2. tags: [tag1, tag2, tag3] (array/list)
            # 3. tags: tag1, tag2, tag3 (comma-separated string)
            tags = metadata['tags']
            if isinstance(tags, list):
                return [tag.strip().lower() for tag in tags]
            elif isinstance(tags, str):
                # Check if comma-separated
                if ',' in tags:
                    return [tag.strip().lower() for tag in tags.split(',')]
                # Space-separated
                return [tag.strip().lower() for tag in tags.split()]
            else:
                return [str(tags).lower()]
        except yaml.YAMLError:
            print(f"Error parsing YAML front matter in {file_path}")
            return []
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def main():
    blog_root = os.path.dirname(os.path.abspath(__file__))
    posts_dir = os.path.join(blog_root, "_posts")
    tags_file = os.path.join(blog_root, ".tags")
    
    all_tags = set()
    file_tags = {}  # Dictionary to store tags from each file
    
    # Count total markdown files for progress reporting
    total_files = 0
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
    
    print(f"Found {total_files} markdown files to process")
    
    # Process each markdown file
    processed_files = 0
    start_time = time.time()
    
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                processed_files += 1
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, blog_root)
                
                # Show progress
                progress = (processed_files / total_files) * 100
                elapsed = time.time() - start_time
                print(f"[{processed_files}/{total_files}] {progress:.1f}% - Processing {relative_path}", end="")
                
                # Extract tags
                tags = extract_tags_from_md(file_path)
                
                if tags:
                    file_tags[relative_path] = tags
                    all_tags.update(tags)
                    print(f" - Found tags: {', '.join(tags)}")
                else:
                    print(" - No tags found")
    
    # Sort tags alphabetically
    sorted_tags = sorted(all_tags)
    
    # Write to .tags file
    with open(tags_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted_tags))
    
    # Print summary
    elapsed_total = time.time() - start_time
    print(f"\nProcessing completed in {elapsed_total:.2f} seconds")
    print(f"Extracted {len(sorted_tags)} unique tags to {tags_file}")
    
    # Print tag statistics
    tag_usage = {}
    for tags_list in file_tags.values():
        for tag in tags_list:
            tag_usage[tag] = tag_usage.get(tag, 0) + 1
    
    print("\nTag usage statistics:")
    for tag, count in sorted(tag_usage.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tag}: {count} files")
    
    # Optional: Generate a report file with details
    report_file = os.path.join(blog_root, "tags_report.txt")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"Tags Report\n")
        f.write(f"==========\n\n")
        f.write(f"Total unique tags: {len(sorted_tags)}\n")
        f.write(f"Total files processed: {total_files}\n")
        f.write(f"Files with tags: {len(file_tags)}\n\n")
        
        f.write("Tag occurrences:\n")
        for tag, count in sorted(tag_usage.items(), key=lambda x: x[1], reverse=True):
            f.write(f"  {tag}: {count} files\n")
        
        f.write("\nTags by file:\n")
        for file_path, tags in sorted(file_tags.items()):
            f.write(f"\n{file_path}\n")
            for tag in sorted(tags):
                f.write(f"  - {tag}\n")
    
    print(f"\nDetailed report saved to {report_file}")

if __name__ == "__main__":
    main()
