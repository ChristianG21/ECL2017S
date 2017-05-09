#! /usr/bin/env python

# input /data/cells.mat
# output /results/
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import sys
import os

basepath = os.getcwd()[0:(len(os.getcwd())-4)]
data = sio.loadmat(basepath + sys.argv[1])['cells']
print(data[0,37,15,1])


# Plots
for t in [0]:
	fig = plt.figure(figsize=(10,7))
	for z in range(1,17):
		plt.subplot(4,4,z)
		plt.imshow(data[:,:,z-1,t])
		plt.title('Z = '+ str(z))

	#plt.axis('off')		
	plt.subplots_adjust(left=.1, bottom=None, right=.8, top=None, wspace=None, hspace=None)
	cax = plt.axes([0.825, 0.1, 0.035, 0.8])
	#plt.colorbar(cax=cax)
	if t < 3:
		plt.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(t*2 + 10))
	else:
		plt.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(t*2 + 8))
	fig.text(0.5, 0.04, 'Voxel Number in X Direction', ha='center', va='center')
	fig.text(0.06, 0.5, 'Voxel Number in Y Direction', ha='center', va='center', rotation='vertical')
	fig.text(0.95, 0.5, 'Tumor Cell Count Per Voxel', ha='center', va='center', rotation='vertical')
	plt.show()
