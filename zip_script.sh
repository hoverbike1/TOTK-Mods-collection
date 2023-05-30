#!/bin/bash

version="$1"

# Find folders containing config.yaml
folders=$(find . -type f -name "config.yaml" -exec dirname {} \;)

# Iterate through the folders
for folder in $folders; do
  # Check if config.yaml contains "game: version"
  if grep -q "game: version" "$folder/config.yaml"; then
    # Get the version number
    config_version=$(grep "game: version" "$folder/config.yaml" | awk '{print $2}')

    # Compare the version numbers
    if [ "$config_version" = "$version" ]; then
      # Create a zip file with the version number
      zip -r "$folder-$version.zip" "$folder"

      echo "Created $folder-$version.zip"
    fi
  fi
done
