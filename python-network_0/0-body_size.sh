#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract the URL from the argument
URL="$1"

# Send a HEAD request to the URL using curl, get the size of the response body in bytes
CONTENT_LENGTH=$(curl -sI "$URL" | grep -i "Content-Length:" | awk '{print $2}')

# If Content-Length is empty, handle the case
if [ -z "$CONTENT_LENGTH" ]; then
    echo "Content-Length not provided in response headers."
else
    echo "$CONTENT_LENGTH"
fi

