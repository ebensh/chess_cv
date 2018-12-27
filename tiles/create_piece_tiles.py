#!/usr/bin/env python3

import argparse
import os.path
import sys

import numpy as np
import cv2


def main(filename, left, top, width, height):
  img = cv2.imread(filename, cv2.IMREAD_COLOR)
  w = width / 8
  h = height / 8

  # 0, 0 is the top left! row, column != rank, file.
  def get_tile_img(r, c):
    x1 = int(left + w * c)
    x2 = int(left + w * (c + 1))
    y1 = int(top + h * r)
    y2 = int(top + h * (r + 1))
    print(x1, x2, y1, y2)
    return img[y1:y2, x1:x2, :]

  # Assume player is white.
  white_piece_row, white_pawn_row = 7, 6
  black_piece_row, black_pawn_row = 0, 1
  if np.sum(get_tile_img(0, 4)) < np.sum(get_tile_img(7, 4)):
    # Player is actually black, so flip.
    white_piece_row, white_pawn_row = 0, 1
    black_piece_row, black_pawn_row = 7, 6

  tile_light = get_tile_img(3, 3)
  tile_dark = get_tile_img(3, 4)
  # TODO: continue here


  cv2.imwrite('white_rook_on_light.png', get_tile_img(white_piece_row, 0))
  cv2.imwrite('white_knight_on_dark.png', get_tile_img(white_piece_row, 1))
  cv2.imwrite('white_bishop_on_light.png', get_tile_img(white_piece_row, 2))
  cv2.imwrite('white_king_on_dark.png', get_tile_img(white_piece_row, 3))
  cv2.imwrite('white_queen_on_light.png', get_tile_img(white_piece_row, 4))
  cv2.imwrite('white_bishop_on_dark.png', get_tile_img(white_piece_row, 4))

  tile = get_tile_img(0, 1)
  print(tile.shape)
  cv2.imshow('img', get_tile_img(0, 1))
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
      description='Given an initial chess board create piece tile images.')
  parser.add_argument("-i", dest="filename", required=True,
                      help="Input image with chess board.", metavar="<input file>",
                      type=lambda x: is_valid_file(parser, x))
  parser.add_argument("-left", dest="left", type=int, required=True,
                      help="x-coordinate of top left corner of chess board.")
  parser.add_argument("-top", dest="top", type=int, required=True,
                      help="y-coordinate of top left corner of chess board.")
  parser.add_argument("-width", dest="width", type=int, required=True,
                      help="width of chess board.")
  parser.add_argument("-height", dest="height", type=int, required=True,
                      help="height of chess board.")
  args = parser.parse_args()
  main(args.filename, args.left, args.top, args.width, args.height)
