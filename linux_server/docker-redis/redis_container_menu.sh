#!/bin/bash

# Define the container name
container_name="redis"

# function to display the menu options
function display_menu {
    echo "Docker Container Menu"
    echo "------------------------"
    echo "0. Rebuild Docker Container"
    echo "1. Build Docker Image"
    echo "2. Stop and Remove Docker Container and Image"
    echo "------------------------"
}

display_menu
read -p "Enter your choice [0-2]: " choice
case $choice in
    0|"")
        echo "Rebuilding Docker Container..."
        docker stop $container_name
        docker rm $container_name
        docker rmi img-$container_name
        docker build . -t img-$container_name
        ;;
    1)
        echo "Building Docker Image..."
        docker build . -t img-$container_name
        docker compose up -d
        ;;
    2)
        echo "Stopping and Removing Docker Container and Image..."
        docker stop $container_name
        docker rm $container_name
        docker rmi img-$container_name
        ;;
    *)
        echo "Invalid choice. Please select an option from the menu."
        ;;
esac

