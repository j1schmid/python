#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, shutil
import xml.etree.ElementTree as et
import datetime


usage_str='''
	usage: eagle_brd_sort_vias.py <file>
	where:
	file:     eagle layout (*.brd) file
	
	Puts all vias inside a signal tag to the end, so the holes of all vias are visible inside a polygon or wire.
	
	KNOWN ISSUE:
	The output is not an exact copy, the header (xml coding and the doctype tag) is missing and the attributes are rearranged in a alphabetic order. Eagle adds the header and rearranges the attributs when the layout is saved.
	
	JSCH 2017-01-05 tested with eagle V7.5.0
	'''

# http://pythoncentral.io/how-to-copy-a-file-in-python-with-shutil/
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)
        
def sort_vias(root):
	for signal in root.iter('signal'):
		print signal.attrib
		for via in signal.findall('via'):
			signal.remove(via)
			signal.append(via)
	return root

def print_usage_and_die(msg):
	print(msg)
	print(usage_str)

if len(sys.argv) != 2:
	print_usage_and_die('error: wrong number of arguments')
	sys.exit()

else:
	
	backupfilename = '{:s}_{:s}'.format(sys.argv[1], datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") )
	infilename = sys.argv[1]
	outfilename = sys.argv[1]
	
	print 'Make backup copy of the layout ({:s}).'.format(backupfilename)
	copyFile(infilename, backupfilename)
	
	tree = et.parse(infilename)
	root = tree.getroot()
	for signal in root.iter('signal'):
		print signal.attrib
		for via in signal.findall('via'):
			signal.remove(via)
			signal.append(via)
	
	print 'Overwrite the layout ({:s}) with the modifed layout.'.format(outfilename)
	tree.write(outfilename)
	#tree.write(filename, encoding='utf-8', xml_declaration=True)
	print('done')
