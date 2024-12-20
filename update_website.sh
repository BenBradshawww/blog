#!/bin/bash

# Step 1: Pull latest changes from the origin
echo "Pulling latest changes from the origin"
git pull origin main

# Step 2: Copy images from obsidian to website
IMAGE_SOURCE_DIR="/Users/benbradshaw/Documents/Obsidian Vault/images/"
IMAGE_TARGET_DIR="/Users/benbradshaw/Documents/Code/website/static/images/"

echo "Copying blogs from obsidian to "
rsync -avh "$IMAGE_SOURCE_DIR" "$IMAGE_TARGET_DIR"

if [ $? -eq 0 ]; then
    echo "rsync completed successfully!"
else
    echo "rsync failed."
    exit 1
fi


# Step 3: Save blog metadata
echo "Saving blog metadata"
python save_blog_metadata.py

if [ $? -ne 0 ]; then
    echo "Python script failed. Exiting."
    exit 1
fi


# Step 4: Copy blogs from obsidian to website
BLOG_SOURCE_DIR="/Users/benbradshaw/Documents/Obsidian Vault/posts/"
BLOG_TARGET_DIR="/Users/benbradshaw/Documents/Code/website/content/en/"

echo "Copying blogs from obsidian to "
rsync -avh "$BLOG_SOURCE_DIR" "$BLOG_TARGET_DIR"

if [ $? -eq 0 ]; then
    echo "rsync completed successfully!"
else
    echo "rsync failed."
    exit 1
fi

# Step 5: Update blog with its metadata
echo "Adding blog metadata"
python add_blog_metadata.py

if [ $? -ne 0 ]; then
    echo "Python script failed. Exiting."
    exit 1
fi

# Step 6: Confirm that all manaul changes with the blog metadata have been written.
while true; do
    read -p "Type 'Y' if you have finished adding additional metadata:" input
    if [[ "$input" == "Y" ]]; then
        echo "Thank you! Proceeding..."
        break
    else
        echo "Invalid input. Please type 'Y'."
    fi
done

# Step 7: Updating main branch
echo "Updating public directory"
hugo   

echo "www.mathstoml.com" > public/CNAME

echo "Committing changes"
git add .

git commit -m "Update blogs"

echo "Pushing changes to the origin"
git push origin main

# Step 8: Update deployment branch
echo "Updating public branch"
git subtree split --prefix public -b deploy

git push origin deploy -f

git branch -D deploy

# Process completed
echo "Process completed. Changes pushed to both main and public branch"