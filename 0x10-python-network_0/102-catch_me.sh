#!/bin/bash
# A Bash Script used to make a request to 0.0.0.0:5000/catch_me
# Gets the message "You got me!".
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
