#!/bin/bash
#A Bash Script used to send a request to a URL passed as an argument to display the status code of the response only.
curl -s -o /dev/null -w "%{http_code}" "$1"
