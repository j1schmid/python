#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(
		prog = 'ProgramName',
		description = 'What the program does',
		epilog = 'Text at the bottom of help')

parser.add_argument('filename')										# positional argument
parser.add_argument('-c', '--count')								# option that takes a value
parser.add_argument('-v', '--verbose', action='store_true') 		# on/off flag

#import code # entering the interactive mode at a certain point: code.interact(local=dict(globals(), **locals())), Ctrl+D and the script goes on


def main(cfg):
	print(cfg)
    

if __name__ == '__main__':
	cfg = parser.parse_args()
	main(cfg)
