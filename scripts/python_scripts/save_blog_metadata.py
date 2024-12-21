import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

blog_directory = './content/en/'
metadata_directory = './content/en/metadata/'


def extract_metadata(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        metadata = []
        updated_lines = []
        started = False
        found_all_metadata = False
        for line in lines:
            if line.strip() == "+++":
                if started:
                    found_all_metadata = True
                    metadata.append(line)
                else:
                    started = True
                    metadata.append(line)

            elif started and not found_all_metadata:
                metadata.append(line)

            elif found_all_metadata:
                updated_lines.append(line)

            
        if started:
            base_name = file_path.split('/')[-1][:-3]
            output_file_path = os.path.join(metadata_directory, f"{base_name}_metadata.txt")

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(metadata)

            logger.info(f"Metadata extracted and saved to: {output_file_path}")

            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(updated_lines)
            
            logger.info(f"{file_path.split('/')[-1]} updated to exclude metadata")
        else:
            logger.info(f"No metadata found in: {file_path}")
        

def save_metadata():
    os.makedirs(metadata_directory, exist_ok=True)
    for file in os.listdir(blog_directory):
        if file == "metadata":
            continue
        file_path = blog_directory + file
        logger.info(f"Saving metadata from {file}")
        extract_metadata(file_path)

if __name__ == "__main__":
    save_metadata()
