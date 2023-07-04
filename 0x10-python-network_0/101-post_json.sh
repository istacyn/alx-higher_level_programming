#!/bin/bash
# Sends a JSON POST request and dispalys response body
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
