#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#import code # entering the interactive mode at a certain point: code.interact(local=dict(globals(), **locals())), Ctrl+D and the script goes on


usage_str='''
Usage: ./eagle_bom_to_ssp.py FILE
.....
.
'''
def main():
    if len(sys.argv) != 2:
		print('error: wrong number of arguments')
		print(usage_str)
		sys.exit()


if __name__ == '__main__':
	main()
