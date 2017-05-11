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
for t in [0,1,2,3,4,5,6]:
	fig = plt.figure(figsize=(12,8))
	znum = 0
	for z in [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19]:
		plt.subplot(4,5,z)
		plt.imshow(data[:,:,znum,t])
		plt.tick_params(axis='both',length=0)
		plt.title('Z = '+ str(znum+1), weight='bold')
		znum += 1
	plt.subplot(4,5,20).set_visible(False)
	fakedata = np.array([[0,40000],[0,40000]])
	plt.imshow(fakedata)		
	plt.subplots_adjust(left=.1, bottom=None, right=1, top=None, wspace=None, hspace=None)
	cax = plt.axes([0.825, 0.1, 0.035, 0.8])
	plt.colorbar(cax=cax,format='%1.1e')
	if t < 3:
		plt.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(t*2 + 10), weight='bold')
	else:
		plt.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(t*2 + 8), weight='bold')
	fig.text(0.5, 0.04, 'Voxel Number in X Direction', ha='center', va='center')
	fig.text(0.06, 0.5, 'Voxel Number in Y Direction', ha='center', va='center', rotation='vertical')
	fig.text(0.95, 0.5, 'Tumor Cell Count Per Voxel', ha='center', va='center', rotation='vertical')
	for ax in plt.gcf().axes:
		try:
			ax.label_outer()
		except:
			pass
plt.show()