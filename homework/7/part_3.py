#! /usr/bin/env python
import sys
if len(sys.argv) != 3: # check the number of arguments to be exactly 2.
        print("\nUsage:\n         ./readDSSP.py <input dssp file> <output summary file>\n\nProgram aborted.")
        sys.exit()
amino = open(sys.argv[1],'r')
rows = amino.readlines()
surfAtotal = dict( [ ('A', 129.0) \
					,('R', 274.0) \
					,('N', 195.0) \
					,('D', 193.0) \
					,('C', 167.0) \
					,('Q', 225.0) \
					,('E', 223.0) \
					,('G', 104.0) \
					,('H', 224.0) \
					,('I', 197.0) \
					,('L', 201.0) \
					,('K', 236.0) \
					,('M', 224.0) \
					,('F', 240.0) \
					,('P', 159.0) \
					,('S', 155.0) \
					,('T', 172.0) \
					,('W', 285.0) \
					,('Y', 263.0) \
					,('V', 174.0) ] )
amina = open(sys.argv[2], 'w')
amina.write("pdb     name    ACC     RSA\n")
for k in range(25, len(rows)):
	J = rows[k]
	if J[13] != "!":
		amina.write('{}  {}       {:>3}     {}\n' .format(sys.argv[1][2:8],J[13],int(J[34:38]),(int(J[34:38])/(surfAtotal[J[13]]))))
amina.close()
amino.close()