#!/bin/bash

# Example:
# ./extract_frame.sh videos/video.webm 1:00 test.png

ffmpeg -ss $2 -i "$1" -frames:v 1 "$3"