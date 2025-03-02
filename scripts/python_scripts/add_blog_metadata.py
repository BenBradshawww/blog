import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

blog_directory = './content/en/'
blog_directory_2 = '../custom_blog/content/posts/'

blog_sites = [blog_directory, blog_directory_2]

def add_metadata_to_all_blogs():
    metadata_directory = './content/en/metadata/'
    for file in os.listdir(metadata_directory):
        if file == "metadata":
            continue
        file_path = metadata_directory + file
        logger.info(f"Adding metadata to {file}")
        add_metadata(file_path)


def add_metadata(metadata_path):
    filename = metadata_path.split('/')[-1][:-len('_metadata.txt')]

    for blog_directory in blog_sites:
        if blog_directory == blog_directory_2 and "about_me" in filename:
            continue # No about me page in dev blog
        blog_path = os.path.join(blog_directory, filename + '.md')

        with open(metadata_path, 'r') as f:
            metadata_content = f.read()
        
        with open(blog_path, 'r') as f:
            existing_content = f.read()

        with open(blog_path, 'w') as f:
            f.write(metadata_content + '\n' + existing_content)

        logger.info(f"Metadata added to {filename} in {blog_directory}")

if __name__ == "__main__":
    add_metadata_to_all_blogs()
