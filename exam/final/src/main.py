#! /usr/bin/env python
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import sys
import os

# Saving data to an array.
basepath = os.getcwd()[0:(len(os.getcwd())-4)] # Saves the main directory you're running this script from, sans /src/
data = sio.loadmat(basepath + sys.argv[1])['cells'] # Loads the .mat file to "data" for future use.

# First Set of Plots.
for t in [0,1,2,4,5,6]: # Goes through plots for all times.
	fig = plt.figure(figsize=(12,8))
	znum = 0 # Goes through every z coordinate
	for z in [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19]: # Places data in all subplots. I hacked a way for the colorbar to be
		plt.subplot(4,5,z)								# how I wanted, ignore the fact that there are 20 subplots.
		plt.imshow(data[:,:,znum,t]) # Plots all data for given z and t.
		plt.tick_params(axis='both',length=0) # Gets rid of ticks
		plt.title('Z = '+ str(znum+1), weight='bold')
		znum += 1
	plt.subplot(4,5,20).set_visible(False) # Creates subplot but makes it nonvisible
	fakedata = np.array([[0,40000],[0,40000]]) # Fake data so the colorbar goes from values 0 to 40000.
	plt.imshow(fakedata) # Plots fake data for colorbar to sample because colorbar always samples the last of the subplots for some reason.
	plt.subplots_adjust(left=.1, bottom=None, right=1, top=None, wspace=None, hspace=None) # Move subplots to make room for colorbar
	cax = plt.axes([0.825, 0.1, 0.035, 0.8]) # Choice where to have the colorbar
	plt.colorbar(cax=cax,format='%1.1e') # Create colorbar with reference to the last subplot which is the fakedata subplot that is invisible.
	fig.text(0.5, 0.04, 'Voxel Number in X Direction', ha='center', va='center') 
	fig.text(0.06, 0.5, 'Voxel Number in Y Direction', ha='center', va='center', rotation='vertical')
	fig.text(0.95, 0.5, 'Tumor Cell Count Per Voxel', ha='center', va='center', rotation='vertical')
	for ax in plt.gcf().axes: # Getting rid of axis labels that aren't on the far leftmost or bottommost side.
		try:
			ax.label_outer()
		except:
			pass
	if t < 3: # Title the entire figure, making sure to skip t = 3, because we're not plotting that for some reason.
		plt.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(t*2 + 10), weight='bold')
		plt.savefig(basepath +  sys.argv[2] + 'BrainSlicesT={}.png'.format(t*2 + 10))
	else:
		plt.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(t*2 + 8), weight='bold')
		plt.savefig(basepath +  sys.argv[2] +'BrainSlicesT={}.png'.format(t*2 + 8))	
	plt.close()     # Use this if you want to only save the graph and not have them show.
	#plt.show()     # Use this if you want the graph of every time interval to show up individually. All plots still saved.
#plt.show()     # Use this if you want the graph of every time interval to show up all at the same time. All plots still saved.


# Second Plot.
celltot = np.zeros(7) # Initialize a place to put all the total number of tumor cells for each t.
for t in [0,1,2,3,4,5,6]: # Go through each t and calculate total tumor cells.
	celltot[t] = sum(sum(sum(data[:,:,:,t])))
plt.plot([10,12,14,15,16,18,20],celltot,marker='o')
plt.axis([8,22,0,16e7])
plt.minorticks_on()
plt.xlabel('Time [Days]')
plt.ylabel('Tumor Cell Count')
plt.title('Rat W09. No radiation treatment',weight='bold')
plt.savefig(basepath +  sys.argv[2] + 'TumorCellCount.png')
plt.close()     # Use this if you just want the plot to be saved, not shown.
#plt.show()     # Use this if you want the plot to be saved and shown.

# The really confusing bit.
def N(t,a,b,c): # t is the time data is read from, a/b/c are user choice.
	N = a*np.exp(-b*np.exp(-c*t))
	return N

def Nobs(t): # t is the time data is read from.
	Nobs = sum(sum(sum(data[:,:,:,t-1])))
	return Nobs

def GaussFunc(t,a,b,c,sigma): # t is the time data is read from, a/b/c/sigma are user choice.
	GaussAtOneTime = (1/(sigma*np.pi*np.sqrt(2*np.pi)))*np.exp(-(np.power((Nobs(t)-N(t,a,b,c)),2))/(2*np.power(sigma,2)))
	return GaussAtOneTime

def MainFunc(i,n,a,b,c,sigma): # i= initial time, n= final time, a/b/c/sigma are all user choice.
	GaussOverAllTime = 0
	for t in range(i,n):
		GaussOverAllTime += np.power(GaussFunc(t,a,b,c,sigma),2)
	LLogged = (-n*.5*(np.log(2*np.pi)+(np.log(np.power(sigma,2))))) - (np.power(2*np.power(sigma,2),-1) * GaussOverAllTime)
	LnoLog = np.power(10,LLogged) # Taking L that has a log in front of it to the power of 10 to get rid of the log, you can keep it if you want.
	return LnoLog

L = MainFunc(1,7,1,1,1,2) # Sample of the main function, with a/b/c/sigma = 1.
print('The value I got from part 3 is {}.'.format(L))