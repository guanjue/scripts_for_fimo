def fasta2matrix(input):
	data=open(input,'r')	
	data_seq_A=open(input+".A.txt",'w')
	data_seq_T=open(input+".T.txt",'w')
	data_seq_C=open(input+".C.txt",'w')
	data_seq_G=open(input+".G.txt",'w')
	#seq_cor=open(input+".seq_coor.txt",'w')

	for records in data:	
		s=list(records)
		if s[0]=='>':
			#seq_cor.write(records)
			for j in range(1,len(s)-1):
				data_seq_A.write(s[j])
				data_seq_T.write(s[j])
				data_seq_C.write(s[j])
				data_seq_G.write(s[j])
			data_seq_A.write('\t')
			data_seq_T.write('\t')
			data_seq_C.write('\t')
			data_seq_G.write('\t')
		else:
			for i in range(0,len(s)):
				## write 'A' matrix
				if s[i].upper()=='A':
					data_seq_A.write('1'+'\t')
					data_seq_T.write('0'+'\t')
					data_seq_C.write('0'+'\t')
					data_seq_G.write('0'+'\t')
				## write 'T' matrix
				elif s[i].upper()=='T':
					data_seq_A.write('0'+'\t')
					data_seq_T.write('1'+'\t')
					data_seq_C.write('0'+'\t')
					data_seq_G.write('0'+'\t')
				## write 'C' matrix
				elif s[i].upper()=='C':
					data_seq_A.write('0'+'\t')
					data_seq_T.write('0'+'\t')
					data_seq_C.write('1'+'\t')
					data_seq_G.write('0'+'\t')
				## write 'G' matrix
				elif s[i].upper()=='G':
					data_seq_A.write('0'+'\t')
					data_seq_T.write('0'+'\t')
					data_seq_C.write('0'+'\t')
					data_seq_G.write('1'+'\t')	
			data_seq_A.write('\n')
			data_seq_T.write('\n')
			data_seq_C.write('\n')
			data_seq_G.write('\n')
	#seq_cor.close()
	data.close()
	data_seq_A.close()
	data_seq_T.close()
	data_seq_C.close()
	data_seq_G.close()

import getopt
import sys
def main(argv):
		try:
				opts, args = getopt.getopt(argv,"hi:")
		except getopt.GetoptError:
				print('fasta2matrix.py -i < input fasta file >')
				sys.exit(2)

		for opt,arg in opts:
				if opt=="-h":
						print('fasta2matrix.py -i <input fasta file>')
						sys.exit()
				elif opt=="-i":
						input=str(arg.strip())
		fasta2matrix(input)

if __name__=="__main__":
		main(sys.argv[1:])

#e.g. python fasta2matrix.py -i test.fa 

