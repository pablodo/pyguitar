#! /usr/bin/python
import argparse

from scales import make_scale
from board import Board

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tunning', type=str, 
                    help='Guitar tunning', default='EADGBE')
parser.add_argument('-k', '--key', type=str, 
                    help='Key note of the scale', required=True)
parser.add_argument('-s', '--scale', type=str, 
                    help='Scale to draw', required=True)
args = parser.parse_args()

note = args.key.lower()
scale = args.scale.lower()

scale_notes = make_scale(note, scale)
board = Board()
print board.draw(scale_notes)
