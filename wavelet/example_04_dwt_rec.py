#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import pdb
import pywt
from numpy import genfromtxt


def plot_dwt_rec(signal,coeffs,wavelet):
	fig = plt.figure()
	N = len(coeffs)
	
	graph = fig.add_subplot(N,1,1)
	graph.plot(signal)
	graph.set_title('signal')
	
	#idwt
	
	for m in range(2,N+1):
		graph = fig.add_subplot(N,1,m)
		graph.plot(pywt.waverec(coeffs[0:m], wavelet))
		graph.set_title('v_{:d}'.format(m))
		
	graph.plot(pywt.waverec(coeffs, wavelet))
	
	graph.set_title('u_{:d}'.format(N-2))
	plt.show()

def main():

	LEVEL = 4
	
	my_data = genfromtxt('data/signals1.csv', delimiter=',')
	
	x = my_data[:,0] # rectangular
	x = my_data[:,1] # sin(t) inclusiv jump
	x = my_data[:,2] # sin(t) diff. freq. and jump
	x = my_data[:,3] # rect, sin
	n = np.linspace(0,1.5*np.pi,196)
	x = np.sin(n*2)
	
	wavelet = pywt.Wavelet('haar')
	
	[phi, psi, _] = wavelet.wavefun(5)
	fig = plt.figure()
	graph = fig.add_subplot(111)
	graph.plot(psi)
	graph.plot(phi)
	plt.show()
	
	coeffs = pywt.wavedec(x, wavelet, level=LEVEL)
	#pdb.set_trace()

	plot_dwt_rec(x,coeffs,wavelet)
	#for m in range(1,LEVEL):
		
	
	pdb.set_trace()

if __name__ == '__main__':
	main()
