#!/bin/bash

# task-2.sh - Setup DVC and track raw data

# Fail fast
set -e

# Step 1: Initialize DVC
echo "Initializing DVC..."
dvc init

# Step 2: Configure local remote
REMOTE_PATH="/Users/yosephabate/dvc-storage"
echo "dvc: Creating local remote at $REMOTE_PATH..."
mkdir -p "$REMOTE_PATH"
dvc remote add -d localstorage "$REMOTE_PATH"

echo "dvc: Committing DVC init and config..."
git add .dvc .dvcignore .gitignore .dvc/config
git commit -m "Initialize and configure DVC with local remote"

# Step 3: Track the dataset
echo "dvc: Tracking dataset with DVC..."
dvc add data/MachineLearningRating_v3.csv

echo "dvc: Committing DVC tracked dataset..."
git add data/MachineLearningRating_v3.csv.dvc
git commit -m "Track MachineLearningRating_v3.csv with DVC"

# Step 4: Push data to local remote
echo "Pushing data to DVC remote..."
dvc push

echo "✅ Task-2 DVC setup complete!"
