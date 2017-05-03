import matplotlib.pyplot as plt
import urllib.request as urlr
import numpy as np
import sys
import os
from parseTable import parseTable

link = sys.argv[1]
outputPath = sys.argv[2]

def fetchHtmlTable(link,outputPath):
	# Creating directory if it does not exist
	if not os.path.exists(outputPath+'/Gamma-Ray Burst Data/'):
		os.makedirs(outputPath+'/Gamma-Ray Burst Data/')
	# Outputting HTML
	urlr.urlretrieve(link,filename=outputPath+'/Gamma-Ray Burst Data/'+'bat_time_table.html')
	# Outputting table
	tableout = open(outputPath+'/Gamma-Ray Burst Data/'+'bat_time_table.html.tab','w')
	for row in parseTable(((urlr.urlopen(link)).read()).decode()):
		for column in row:
			tableout.write( '{:>30}'.format(column))
		tableout.write('\n')
	tableout.close()

def ep_fluFileTester():
	# Creating ep_flu_files directory if it does not exist
	if not os.path.exists(outputPath+'/Gamma-Ray Burst Data/'+'ep_flu_files'):
		os.makedirs(outputPath+'/Gamma-Ray Burst Data/'+'ep_flu_files')
    # Doing work
	ogtable = open(outputPath+'/Gamma-Ray Burst Data/'+'bat_time_table.html.tab','r')
	row = ogtable.readlines()
	for k in range(1,len(row)):
		ID = row[k]
		try:
			urlr.urlretrieve('http://www.shahmoradi.org/ECL2017S/homework/9/swift/GRB'+ID[21:29]+'_ep_flu.txt',filename=outputPath+'/Gamma-Ray Burst Data/'+'ep_flu_files/'+ID[7:17]+'_ep_flu.txt')
		except urlr.HTTPError:
			continue
	ogtable.close()

def plotBatFiles(inPath,figFile):

	ax = plt.gca()  # generate a plot handle
	ax.set_xlabel('Fluence [ergs/cm^2]') # set X axis title
	ax.set_ylabel('Epeak [keV]')  # set Y axis title
	ax.set_xscale('log')
	ax.set_yscale('log')
	ax.axis([1.0e-8, 1.0e-1, 1.0, 1.0e4]) # set axix limits [xmin, xmax, ymin, ymax]
	counter = 0     # counts the number of events
	for file in os.listdir(inPath):
		if file.endswith("ep_flu.txt"):
			data = np.loadtxt(os.path.join(inPath, file), skiprows=1)
			if data.size!=0 and all(data[:,1]<0.0):
				data[:,1] = np.exp(data[:,1])
				ax.scatter(data[:,1],data[:,0],s=1,alpha=.05,c='r',edgecolors='none')
		counter += 1
	ax.set_title('Plot of Epeak vs. Fluence for {} Swift GRB events'.format(counter))
	plt.savefig(figFile)
	plt.show()

fetchHtmlTable(link,outputPath)
ep_fluFileTester()
plotBatFiles(outputPath+'/Gamma-Ray Burst Data/'+'ep_flu_files/',outputPath+'/Gamma-Ray Burst Data/GRBData')