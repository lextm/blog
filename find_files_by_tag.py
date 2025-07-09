#!/usr/bin/env python3

import os
import re
import yaml
import sys
import argparse
from pathlib import Path

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
            
            # Handle different tag formats
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

def find_files_by_tag(tag, posts_dir):
    """Find all files that contain the specified tag."""
    matching_files = []
    
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                tags = extract_tags_from_md(file_path)
                
                if tag.lower() in tags:
                    matching_files.append(file_path)
    
    return matching_files

def list_all_tags(posts_dir):
    """List all available tags in the blog posts."""
    all_tags = set()
    
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                tags = extract_tags_from_md(file_path)
                all_tags.update(tags)
    
    return sorted(all_tags)

def main():
    parser = argparse.ArgumentParser(description='Find blog posts containing specific tags')
    parser.add_argument('tag', nargs='?', help='The tag to search for')
    parser.add_argument('--list-tags', action='store_true', help='List all available tags')
    args = parser.parse_args()
    
    blog_root = os.path.dirname(os.path.abspath(__file__))
    posts_dir = os.path.join(blog_root, "_posts")
    
    # Check if _posts directory exists
    if not os.path.isdir(posts_dir):
        print(f"Error: Posts directory not found at {posts_dir}")
        return 1
    
    # List all available tags if requested
    if args.list_tags:
        tags = list_all_tags(posts_dir)
        print("\nAvailable tags:")
        for tag in tags:
            print(f"  {tag}")
        return 0
    
    # Check if tag argument is provided
    if not args.tag:
        print("Please provide a tag to search for, or use --list-tags to see all available tags.")
        print("Usage: python find_files_by_tag.py <tag>")
        return 1
    
    # Find files with the specified tag
    tag = args.tag
    matching_files = find_files_by_tag(tag, posts_dir)
    
    if matching_files:
        print(f"\nFound {len(matching_files)} files with tag '{tag}':")
        for file_path in matching_files:
            # Print full path
            print(f"  {os.path.abspath(file_path)}")
            
            # Extract and print title from the file (optional)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
                if match:
                    front_matter = match.group(1)
                    metadata = yaml.safe_load(front_matter)
                    if metadata and 'title' in metadata:
                        print(f"    Title: {metadata['title']}")
                print()  # Empty line for better readability
            except:
                pass
    else:
        print(f"\nNo files found with tag '{tag}'")
        
        # Suggest similar tags
        all_tags = list_all_tags(posts_dir)
        similar_tags = [t for t in all_tags if tag.lower() in t.lower()]
        
        if similar_tags:
            print("\nDid you mean one of these tags?")
            for similar_tag in similar_tags:
                print(f"  {similar_tag}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
