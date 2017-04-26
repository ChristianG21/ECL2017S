import sys
from parseTable import parseTable
import urllib.request as urlr

link = sys.argv[1]
outputPath = sys.argv[2]

def fetchHtmlTable(link,outputPath):
	#Outputting HTML
	urlr.urlretrieve(link,filename=outputPath+'bat_time_table.html')
	#Outputting table
	tableout = open(outputPath+'bat_time_table.html.tab','w')
	for row in parseTable(((urlr.urlopen(link)).read()).decode()):
		for column in row:
			tableout.write( '{:>30}'.format(column))
		tableout.write('\n')
	tableout.close()

def ep_fluFileTester():
	ogtable = open(outputPath+'bat_time_table.html.tab','r')
	row = ogtable.readlines()
	for k in range(1,len(row)):
		ID = row[k]
		print(ID[21:29])
		urlr.urlretrieve('http://butler.lab.asu.edu/swift/'+ID[21:29]+'/bat/ep_flu.txt',filename=outputPath+'fuck')
	print(len(row))

fetchHtmlTable(link,outputPath)
ep_fluFileTester()