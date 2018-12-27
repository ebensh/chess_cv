#!/usr/bin/env python3

import argparse
import os.path
import sys

import numpy as np
import cv2

# https://stackoverflow.com/a/11541450


def main(filename, outfile):
  img = cv2.imread(filename, cv2.IMREAD_COLOR)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 50, 150, apertureSize=3)
  lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180,
                          threshold=100, lines=np.array([]),
                          minLineLength=100, maxLineGap=80)
  lines = lines.reshape(lines.shape[0], lines.shape[2])
  vertical_lines = lines[np.abs(lines[:,2] - lines[:, 0]) < 5,:]
  horizontal_lines = lines[np.abs(lines[:,3] - lines[:, 1]) < 5,:]
  vertical_lines = vertical_lines[np.argsort(vertical_lines[:,0])]
  horizontal_lines = horizontal_lines[np.argsort(horizontal_lines[:,1])]

  x = vertical_lines[0, 0]
  y = horizontal_lines[0, 1]
  width = vertical_lines[8, 0] - x
  height = horizontal_lines[8, 1] - y
  print(x, y, width, height)

  cv2.imshow('edges', edges)
  cv2.imshow('img', img)
  while True:
    if cv2.waitKey(0) == ord('q'):
      return

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
