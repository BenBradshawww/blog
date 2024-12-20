# Step 1: Updating main branch
echo "Updating public directory"
hugo   

echo "www.mathstoml.com" > public/CNAME

echo "Committing changes"
git add .

git commit -m "Update website"

echo "Pushing changes to the origin"
git push origin main

# Step 2: Update deployment branch
echo "Updating public branch"
git subtree split --prefix public -b deploy

git push origin deploy -f

git branch -D deploy

# Process completed
echo "Process completed. Changes pushed to both main and public branch"