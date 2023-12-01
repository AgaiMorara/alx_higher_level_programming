#!/usr/bin/env bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | awk 'tolower($1) == "content-length:" {print $2}'


