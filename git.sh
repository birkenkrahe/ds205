#!/bin/bash

git add .
git commit -m "Update from lenovo"
git push
#!/bin/bash

# Your GitHub username and PAT
USERNAME="birkenkrahe"
PAT="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"

# Your repository URL without credentials
# Make sure to replace this with your actual repository URL
REPO_URL="https://github.com/birkenkrahe/your-repo-name.git"

# Extract the domain and path from the URL
REPO_DOMAIN=$(echo "$REPO_URL" | awk -F/ '{print $3}') # e.g., github.com
REPO_PATH=$(echo "$REPO_URL" | cut -d/ -f4-) # e.g., birkenkrahe/your-repo-name.git

# Construct the URL with credentials
REPO_URL_WITH_CREDENTIALS="https://${USERNAME}:${PAT}@${REPO_DOMAIN}/${REPO_PATH}"

# Set remote URL with credentials
git remote set-url origin "${REPO_URL_WITH_CREDENTIALS}"

# Add, commit, and push changes
git add .
git commit -m "Update from lenovo"
git push origin main # or replace 'main' with your branch name if different

# Reset the remote URL to the original one (optional but recommended for security)
git remote set-url origin "${REPO_URL}"
