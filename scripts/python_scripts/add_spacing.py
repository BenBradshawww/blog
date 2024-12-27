import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

blog_directory = './content/en/'

def add_spacing_to_file(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()

    processed_lines = []
    prev_line = None

    for line in lines:

        line = line.strip()

        if line.startswith("$$") and prev_line is not None and prev_line != "": 
            processed_lines.append(f"\n")
        
        processed_lines.append(f"{line}\n")
        
        prev_line = line
    
    with open(file_path, "w") as outfile:
        outfile.writelines(processed_lines)


def add_spacing():
    for file in os.listdir(blog_directory):
        file_path = blog_directory + file
        if file.endswith(".md"):
            logger.info(f"Adding spacing to {file}")
            add_spacing_to_file(file_path)


if __name__ == "__main__":
    add_spacing()