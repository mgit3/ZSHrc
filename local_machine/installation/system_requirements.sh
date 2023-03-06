#!/bin/bash

# Define the list of packages to be installed
myArray=("crontab" "speedtest-cli")

# Show the menu to the user
echo "Choose a package manager:"
echo "1. apt"
echo "2. dnf"

# Read the user's choice
read -p "Enter your choice: " choice

# Check the user's choice and set the appropriate package manager
if [ "$choice" == "1" ]; then
    package_manager="apt-get"
elif [ "$choice" == "2" ]; then
    package_manager="dnf"
else
    # If the choice is invalid, show an error message and exit
    echo "Invalid choice. Exiting."
    exit 1
fi

# Loop through the packages and install each one using the chosen package manager
for pkg in ${myArray[@]}; do
    sudo $package_manager install -y $pkg 
done

