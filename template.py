#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

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
