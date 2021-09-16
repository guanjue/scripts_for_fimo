import numpy as np

################################################################################################
### read 2d array
def read2d_array(filename,dtype_used):
	import numpy as np
	data=open(filename,'r')
	data.readline()
	data0=[]
	for records in data:
		tmp = [x.strip() for x in records.split('\t')]
		data0.append(tmp)
	data0 = np.array(data0,dtype=dtype_used)
	data.close()
	return data0

################################################################################################
### write 2d matrix
def write2d_array(array,output):
	r1=open(output,'w')
	for records in array:
		for i in range(0,len(records)-1):
			r1.write(str(records[i])+'\t')
		r1.write(str(records[len(records)-1])+'\n')
	r1.close()

################################################################################################
### s3norm
def fimo_best_match(fimo_input, fimo_output):
	### read fimo output
	sig1 = read2d_array(fimo_input, str)

	### get dict
	all_dict = {}
	for s in sig1:
		pk_tmp = s[2]
		pval_tmp = float(s[7])
		if not (pk_tmp in all_dict):
			#print(pk_tmp)
			all_dict[pk_tmp] = s
		elif float(all_dict[pk_tmp][7]) > pval_tmp:
			all_dict[pk_tmp] = s

	### write output
	r1=open(fimo_output,'w')
	for pk in all_dict:
		records = all_dict[pk]
		for i in range(0,len(records)-1):
			r1.write(str(records[i])+'\t')
		r1.write(str(records[len(records)-1])+'\n')
	r1.close()	



############################################################################

import getopt
import sys
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hi:o:")
	except getopt.GetoptError:
		print('time python fimo_best_match.py -i fimo_input -o fimo_output')
		sys.exit(2)

	for opt,arg in opts:
		if opt=="-h":
			print('time python fimo_best_match.py -i fimo_input -o fimo_output')
		elif opt=="-i":
			fimo_input=str(arg.strip())
		elif opt=="-o":
			fimo_output=str(arg.strip())

	fimo_best_match(fimo_input, fimo_output)

if __name__=="__main__":
	main(sys.argv[1:])


