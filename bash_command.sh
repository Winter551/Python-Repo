#!/bin/bash

# Check if the website_output.txt file exists
if [ ! -f "website_output.txt" ]; then
    echo "Error: website_output.txt file not found!"
    exit 1
fi

# Read inputs from the website_output.txt file and fuzz the hashcat command
while IFS= read -r website_output; do
    # Define the hashcat command with inputs from website_output.txt
    command_to_fuzz="hashcat -m $website_output -a 0 6e58f76f5be5ef06a56d4eeb2c4dc58be3dbe8c7 rockyou.txt"
    
    # Execute the hashcat command
    echo "Executing: $command_to_fuzz"
    $command_to_fuzz
done < "website_output.txt"
