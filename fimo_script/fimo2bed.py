import numpy as np

################################################################################################
### read 2d array
def read2d_array(filename,dtype_used):
	import numpy as np
	data=open(filename,'r')
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
def fimo2bed(fimo_best_match, fimo_best_match_bed, expand):
	### read fimo output
	sig1 = read2d_array(fimo_best_match, str)

	### get array
	all_bed = []
	for s in sig1:
		pk_tmp = s[2]
		chrom = pk_tmp.split(':')[0]
		start = int(pk_tmp.split(':')[1].split('-')[0])
		end = int(pk_tmp.split(':')[1].split('-')[1])

		motif_start = int(s[3])
		motif_end = int(s[4])

		strand = s[5]

		if strand == '+':
			start_shift = start + motif_start - 1 - expand
			end_shift = start + motif_start - 1 + motif_end - motif_start + expand
		else:
			start_shift = start + motif_start - 1 +1 - expand
			end_shift = start + motif_start - 1 + motif_end - motif_start +1 + expand


		out_bed = [chrom, str(start_shift), str(end_shift), pk_tmp+':'+s[7]+':'+strand, '0', strand]

		all_bed.append(out_bed)

	all_bed = np.array(all_bed)
	### write output
	write2d_array(all_bed, fimo_best_match_bed)


############################################################################

import getopt
import sys
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hi:o:e:")
	except getopt.GetoptError:
		print('time python fimo2bed.py -i fimo_best_match -o fimo_best_match_bed -e expand')
		sys.exit(2)

	for opt,arg in opts:
		if opt=="-h":
			print('time python fimo2bed.py -i fimo_best_match -o fimo_best_match_bed -e expand')
		elif opt=="-i":
			fimo_best_match=str(arg.strip())
		elif opt=="-o":
			fimo_best_match_bed=str(arg.strip())
		elif opt=="-e":
			expand = int(arg.strip())

	fimo2bed(fimo_best_match, fimo_best_match_bed, expand)

if __name__=="__main__":
	main(sys.argv[1:])


