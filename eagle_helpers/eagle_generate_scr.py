#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import csv, sys
#from string import ascii_uppercase

usage_str='''
...
'''

PARTS = 'C1, C15, C16, C17, C18, C23, C24, C25, C26, C27, C28, C34, C37, C38, C39, C40, C41, C42, C43, C44, C45, C46, C47, C48, C51, C55, C56, C57, C67, C68, C69, C70, C82, C98, C103, C104, C118, C125, C126, C127'

PARTS = 'C33, C72, C73'

PARTS = 'C1, C15, C16, C17, C18, C21'

#PARTS = 'C103, C205, C207, C703, C903'
PARTS = 'C209, C506, C509, C510, C704, C705, C706, C816, C819, C904, C905, C906, C1013, C1016, C1412, C1415'

def main():
	print('create eagle script to change package')
	
	
	print('--------------------------------------------------------------')
	for part in PARTS.split(','):
		#print('VALUE {:s} \'1u 25V X7R\';'.format(part))
		print('VALUE {:s} \'1u 25V X7R\';'.format(part))
		#print('CHANGE PACKAGE {:s} C0603K;'.format(part))

	print('--------------------------------------------------------------')


if __name__ == '__main__':
	main()
