#!/bin/bash
# Makes request to 0.0.0.0:5000/catch_me and server responds with message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
