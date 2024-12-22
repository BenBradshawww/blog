# Step 1: Updating main branch
echo "Updating public directory"
hugo build

echo "www.mathstoml.com" > public/CNAME

echo "Committing changes"
git add .

DEFAULT_MESSAGE="Update website"

COMMIT_MESSAGE=${1:-$DEFAULT_MESSAGE}

git commit -m "$COMMIT_MESSAGE"

echo "Pushing changes to the origin"
git push origin main

# Step 2: Update deployment branch
echo "Updating public branch"
git subtree split --prefix public -b deploy

git push origin deploy -f

git branch -D deploy

# Process completed
echo "Process completed. Changes pushed to both main and public branch"