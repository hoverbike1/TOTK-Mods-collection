#!/bin/bash

version="$1"
mods_dir="$2"
format="$3"
zip_file="$version.$format"

# Create a temporary directory to store the compatible config files
temp_dir=$(mktemp -d)

# Find folders containing config.yaml within the Mods directory and its subdirectories
IFS=$'\n' # Set the IFS (Internal Field Separator) to handle folder names with spaces
folders=($(find "$mods_dir" -type f -name "config.yaml" -exec dirname {} \;))

# Iterate through the folders
for folder in "${folders[@]}"; do
  # Read the game versions using yq and store them in an array using mapfile
  result=$(yq e ".game.version[] | select(. == \"$version\")" "$folder/config.yaml")
  if [[ -n $result ]]; then
    # Copy the folder to the temporary directory
    cp -r "$folder" "$temp_dir"
  fi
done

# Create a zip file containing the compatible folders
7z a -t"$format" -mx9 "$zip_file" "$temp_dir"

# Clean up the temporary directory
rm -rf "$temp_dir"

echo "Zip file created: $zip_file"