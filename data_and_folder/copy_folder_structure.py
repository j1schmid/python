#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Replicate/copy folder structure, e.g. to prevent folder sturcture in dataset
# augmentation. Remeber green screen replacement in SynthHands dataset.

import sys, os
from subprocess import check_output
import os

inputpath = 'folder0'
outputpath = 'folder9'

for dirpath, dirnames, filenames in os.walk(inputpath):
	print('dirpath {}; dirnames {}; filenames {}'.format(dirpath, dirnames, filenames))
	structure = os.path.join(outputpath, dirpath[len(inputpath)+1:])
	print ('structure: {}'.format(structure))
	if not os.path.isdir(structure):
		os.mkdir(structure)
	else:
		print("Folder does already exits!")
