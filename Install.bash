#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Display a welcome message
echo "Welcome to the SmartUmpires installation script."
if [dir = "SawyerWetson/SmartUmpires/"]
# Ensure the script is being run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Please run again with sudo." 
   exit 1
fi

# Update and install required dependencies
echo "Updating system and installing dependencies..."
apt-get update -y
apt-get install -y python3 python3-pip git

# Clone the repository if not already cloned
if [ ! -d "SmartUmpires" ]; then
    echo "Cloning the SmartUmpires repository..."
    git clone https://github.com/SawyerWetson/SmartUmpires.git
else
    echo "Repository already cloned."
fi

# Navigate to the repository
cd SmartUmpires

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip3 install -r requirements.txt
else
    echo "No requirements.txt file found. Skipping Python dependency installation."
fi

# Additional setup (if needed)
echo "Performing additional setup..."
# Add commands here for additional setup steps

# Finish
echo "Installation is complete. You can now use the SmartUmpires system."
