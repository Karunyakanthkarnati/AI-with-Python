#!/bin/bash

# Merging all commits and history from the python repository into the AI-with-Python repository

# Initialize a new temporary directory
TEMP_DIR=$(mktemp -d)

# Change to the temporary directory
cd "$TEMP_DIR" || exit

# Clone the source python repository
REPO_URL="https://github.com/<source_owner>/python.git"
git clone "$REPO_URL" source_repo

# Clone the target AI-with-Python repository
REPO_URL="https://github.com/Karunyakanthkarnati/AI-with-Python.git"
git clone "$REPO_URL" target_repo

# Change to the target repository directory
cd target_repo || exit

# Fetch all branches and commits from the source repository
cd ../source_repo || exit
git fetch --all

# Merge the main branch from the source into the main branch of the target repository
cd ../target_repo || exit
git merge --allow-unrelated-histories ../source_repo/main

# Cleanup
rm -rf "$TEMP_DIR"

echo "Successfully merged all commits and history from the python repository into AI-with-Python repository!"