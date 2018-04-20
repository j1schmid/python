#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import numpy as np

class HandPoseSequence:
	
	filename = 'data.csv'
	print('load position file \'{}\''.format(filename))
	
	data = np.genfromtxt(filename, delimiter=',')
	
	print(data)
