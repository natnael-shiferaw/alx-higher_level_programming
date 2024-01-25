#!/bin/bash
#A Bash Script used to send a request to a URL passed as an argument
#Used to display only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
