#!/bin/bash

youtube-dl -f worstvideo $1 -o "videos/%(title)s.%(ext)s"