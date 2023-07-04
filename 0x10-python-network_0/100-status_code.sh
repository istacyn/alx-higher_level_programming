#!/bin/bash
# Sends a request to a URL passed as an argument
# Displays only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
