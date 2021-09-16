def fasta2matrix(input):
	data=open(input,'r')	
	data_seq_categorical=open(input+".categoricalvec.txt",'w')

	for records in data:	
		s=list(records)
		if s[0]=='>':
			#seq_cor.write(records)
			for j in range(1,len(s)-1):
				data_seq_categorical.write(s[j])
			data_seq_categorical.write('\t')
		else:
			for i in range(0,len(s)):
				data_seq_categorical.write(s[i].upper()+'\t')	
			data_seq_categorical.write('\n')
	#seq_cor.close()
	data.close()
	data_seq_categorical.close()

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

