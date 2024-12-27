import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

blog_directory = './content/en/'
metadata_directory = './content/en/metadata/'

def add_metadata_to_all_blogs():
    for file in os.listdir(metadata_directory):
        if file == "metadata":
            continue
        file_path = metadata_directory + file
        logger.info(f"Adding metadata to {file}")
        add_metadata(file_path)


def add_metadata(metadata_path):
    file = metadata_path.split('/')[-1][:-len('_metadata.txt')]
    
    blog_path = os.path.join(blog_directory, file+'.md')

    with open(metadata_path, 'r') as file:
        metadata_content = file.read()
    
    with open(blog_path, 'r') as file:
        existing_content = file.read()

    with open(blog_path, 'w') as file:
        file.write(metadata_content + '\n' + existing_content)

    logger.info(f"Metadata added to {file}")

if __name__ == "__main__":
    add_metadata_to_all_blogs()
