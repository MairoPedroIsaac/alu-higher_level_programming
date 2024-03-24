#!/bin/bash
# Script that shows the Content-Length from a HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f #!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -s "$1" | wc -c2

