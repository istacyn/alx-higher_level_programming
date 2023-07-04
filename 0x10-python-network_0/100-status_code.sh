#!/bin/bash
# Sends request to URL passed, displays status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
