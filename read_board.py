#!/usr/bin/env python3

import argparse
import os.path
import sys

import numpy as np
import cv2

# https://stackoverflow.com/a/11541450


def main(filename, outfile):
  img = cv2.imread(filename, cv2.IMREAD_COLOR)

  cv2.imshow('image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
  def is_valid_file(parser, arg):
    if not os.path.exists(arg):
      parser.error("The file %s does not exist!" % arg)
    else:
      return arg

  parser = argparse.ArgumentParser(
      description='Read a chess board from an image into FEN notation.')
  parser.add_argument("-i", dest="filename", required=True,
                      help="Input image with chess board.", metavar="<input file>",
                      type=lambda x: is_valid_file(parser, x))
  parser.add_argument("outfile", nargs="?", type=argparse.FileType("w"),
                      default=sys.stdout)
  args = parser.parse_args()
  main(args.filename, args.outfile)
