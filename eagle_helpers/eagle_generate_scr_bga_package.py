#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import csv, sys
#from string import ascii_uppercase

usage_str='''
...
'''

#BGA381_ALPHABET = {'A','B','C','D','E','F','G','H','J','K','L','M','N','P','R','T','U','V','W','Y'}
BGA381_ALPHABET = 'ABCDEFGHJKLMNPRTUVWY'
BGA381_NUMBERS = range(1,21)
BGA381_GRID = 0.8

def main():
	
	# create a smd pad with size 0.6x2.3, name '16' at position -0.5 -1.85
	# smd 0.6 2.3 '16' (-0.5 -1.85)
	#
	# create a round smd pad with diameter 0.4mm, name 'A1' at position -0.5 -1.85
	# smd 0.4 0.4 -100 'A1' (-0.5 -1.85)

	print('create eagle script to place smd pads for a BGA package')
	print('381-ball caBGA package')
	
	print('--------------------------------------------------------------')
	print('grid mm;')
	i = 0
	for x in range(0,len(BGA381_NUMBERS)):
		#for y in ascii_uppercase:
		for y in range(0,len(BGA381_ALPHABET)):
			print('smd 0.4 0.4 -100 \'{:s}{:d}\' ({:.2f} {:.2f});'.format(BGA381_ALPHABET[y],BGA381_NUMBERS[x], x*BGA381_GRID, -y*BGA381_GRID));
			i += 1

	print('--------------------------------------------------------------')
	print('{:d} pins'.format(i))


	#with open('ECP5U25Pinout.csv','rb') as csvfile:
		#reader = csv.reader(csvfile,delimiter=';')
		
		#line = reader.next()
		#print(line)
		
		#for row in reader:
			#print(row)
			

	# create a smd pad with size 0.6x2.3, name '16' at position -0.5 -1.85
	# smd 0.6 2.3 '16' (-0.5 -1.85)
	#printf("\n")

#with f = open('caBGA381.scr', 'w'):

if __name__ == '__main__':
	main()
