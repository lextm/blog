import os
import yaml
import logging

# Ensure logging is properly configured
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Include timestamp, level, and message
    handlers=[
        logging.StreamHandler()  # Output logs to the console
    ]
)

# Define the normalize function to standardize text
def normalize(text):
    return text.strip().lower()

# Load categories from .categories file
categories_file = ".categories"
tag_to_category = {}
try:
    with open(categories_file, "r") as file:
        categories_data = yaml.safe_load(file)
        if not isinstance(categories_data, list):
            logging.error(f"Error: '{categories_file}' should contain a list.")
            exit(1)

        # Iterate through the list of categories
        for item in categories_data:
            if isinstance(item, str):
                # Parse the category string which may include tags in the format "Category Name - tag1 - tag2 - tag3"
                parts = item.split(' - ')
                if len(parts) > 1:
                    # First part is the category name, remaining parts are tags
                    category_name = parts[0].strip()
                    tags = [normalize(tag) for tag in parts[1:]]

                    logging.info(f"Processing category: {category_name} with tags: {tags}")

                    # Map each tag to its category
                    for tag in tags:
                        if tag in tag_to_category:
                            logging.warning(f"Duplicate tag '{tag}' found. Assigning to '{category_name}', previously '{tag_to_category[tag]}'.")
                        tag_to_category[tag] = category_name
                else:
                    # Category without tags (like "History")
                    logging.info(f"Processing category: {item} (no tags)")
            elif isinstance(item, list):
                # Skip lists as they aren't expected in this format
                logging.warning(f"Unexpected list found in '{categories_file}'. Structure should be strings only.")
            else:
                logging.warning(f"Skipping unexpected item type in '{categories_file}': {type(item)} - {item}")

    logging.info(f"Successfully built tag-to-category mapping: {tag_to_category}")

except FileNotFoundError:
    logging.error(f"Error: Categories file '{categories_file}' not found.")
    exit(1)
except yaml.YAMLError as e:
    logging.error(f"Error parsing YAML file '{categories_file}': {e}")
    exit(1)
except Exception as e:
    logging.error(f"An unexpected error occurred while processing '{categories_file}': {e}")
    exit(1)


# Define the posts directory
posts_directory = "_posts"

# Function to update categories in a post
def update_post_categories(post_path):
    try:
        with open(post_path, "r", encoding='utf-8') as file:
            lines = file.readlines()
    except Exception as e:
        logging.error(f"Error reading file {post_path}: {e}")
        return

    in_front_matter = False
    front_matter_end_index = -1
    tags_line_index = -1
    categories_line_index = -1
    current_tags = []

    # Parse front matter
    if lines and lines[0].strip() == '---':
        in_front_matter = True
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                front_matter_end_index = i
                break
            if line.startswith("tags:"):
                tags_line_index = i
                try:
                    # Handle tags enclosed in [] or just space-separated (your format)
                    tag_content = line.split(":", 1)[1].strip()
                    if tag_content.startswith('[') and tag_content.endswith(']'):
                        tag_content = tag_content[1:-1] # Remove brackets

                    # Split tags by spaces
                    raw_tags = tag_content.split()
                    current_tags = [normalize(tag) for tag in raw_tags if tag.strip()]
                    logging.info(f"Extracted and normalized tags from {post_path}: {current_tags}")
                except Exception as e:
                    logging.warning(f"Could not parse tags line in {post_path}: {line.strip()} - {e}")
            elif line.startswith("categories:"):
                categories_line_index = i

        if front_matter_end_index == -1:
             logging.warning(f"Front matter started but did not end in {post_path}. Skipping.")
             return
    else:
        logging.warning(f"No front matter found in {post_path}. Skipping.")
        return

    # Count tag matches for each category to determine the best category
    category_match_count = {}
    matched_tags_by_category = {}

    for tag in current_tags:
        if tag in tag_to_category:
            category = tag_to_category[tag]
            if category not in category_match_count:
                category_match_count[category] = 0
                matched_tags_by_category[category] = []

            category_match_count[category] += 1
            matched_tags_by_category[category].append(tag)
            logging.info(f"Tag '{tag}' mapped to category '{category}' for {post_path}")
        else:
            logging.warning(f"Tag '{tag}' from {post_path} did not match any category in the mapping.")

    if not category_match_count:
        logging.info(f"No relevant categories found for tags in {post_path}. No changes made.")
        return

    # Select the best category (the one with the most matching tags)
    best_category = max(category_match_count.items(), key=lambda x: x[1])[0]
    logging.info(f"Selected best category '{best_category}' for {post_path} based on {category_match_count[best_category]} matching tags: {matched_tags_by_category[best_category]}")

    # Format the categories in Jekyll format: [Category1, Category2]
    new_categories_line = f"categories: [{best_category}]\n"

    # Update or insert the categories line
    modified = False
    if categories_line_index != -1:
        # Update existing categories line if different
        if lines[categories_line_index] != new_categories_line:
            logging.info(f"Updating categories line in {post_path} to: {new_categories_line.strip()}")
            lines[categories_line_index] = new_categories_line
            modified = True
        else:
            logging.info(f"Categories line in {post_path} is already correct. No changes needed.")
    elif tags_line_index != -1:
        # Insert categories line after tags line
        logging.info(f"Inserting categories line in {post_path}: {new_categories_line.strip()}")
        lines.insert(tags_line_index + 1, new_categories_line)
        modified = True
    else:
        # Insert categories line at the beginning of front matter (after first '---')
        logging.info(f"Inserting categories line at start of front matter in {post_path}: {new_categories_line.strip()}")
        lines.insert(1, new_categories_line)
        modified = True

    # Write back to the file if modified
    if modified:
        try:
            with open(post_path, "w", encoding='utf-8') as file:
                file.writelines(lines)
            logging.info(f"Successfully updated categories for file: {post_path}")
        except Exception as e:
            logging.error(f"Error writing updated categories to file {post_path}: {e}")


# Main scanning logic
def scan_and_update_categories():
    logging.info("Starting the categorization process.")
    processed_files = 0

    for root, _, files in os.walk(posts_directory):
        logging.info(f"Scanning directory: {root}")
        for file in files:
            if file.endswith(".md"):
                post_path = os.path.join(root, file)
                logging.info(f"Processing markdown file: {post_path}")
                update_post_categories(post_path)
                processed_files += 1 # Increment only after processing a markdown file

    logging.info(f"Categorization process finished. Processed {processed_files} files.")

# Call the main function
scan_and_update_categories()
