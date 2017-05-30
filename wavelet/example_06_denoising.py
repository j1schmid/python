#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import pdb
import pywt
from numpy import genfromtxt
import cv2
import scipy.io


def denoise(data,K,wname,level,threshold_type):
	wavelet = pywt.Wavelet(wname)	
	coeffs = pywt.wavedecn(data,wavelet,level=level)
	# estimate the standard deviation of the noise using the finest detail / nu
	# coefficients
	std_dev = np.median(np.abs(coeffs[-2]['d'])) / 0.6745
	# compute the threshold according to the MSE FTP_Fourier slides week 13
	threshold = K * np.sqrt(2*np.log(len(data))) * std_dev	
	arr, coeff_slices = pywt.coeffs_to_array(coeffs)
	arr = pywt.threshold(arr, threshold, threshold_type)
	coeffs = pywt.array_to_coeffs(arr, coeff_slices)
	return (threshold, pywt.waverecn(coeffs,wavelet))

def show_denoised(data,K,wname,level):
	threshold, dn_hard = denoise(data,K,wname,level,'hard')
	_, dn_soft = denoise(data,K,'bior4.4',level,'soft')
	print('threshold: {:f}'.format(threshold))
	
	fig = plt.figure()
	graph = fig.add_subplot(111)
	graph.plot(data)
	graph.plot(dn_soft)
	graph.plot(dn_hard)
	plt.show()

def main():
	FILENAME='data/EEG1.MAT'
	mat = scipy.io.loadmat(FILENAME)
	meas = mat['sig'][0]
	
	show_denoised(meas,1.0,'bior4.4',3)
	show_denoised(meas,1.0,'bior4.4',8)
	#pdb.set_trace()

if __name__ == '__main__':
	main()
