#!/usr/bin/python

import zipfile
import tempfile


# Main Function 
def VCF_parser(vcf_file_name):
	samples = []
	ref = []
	alt = []
	alleles = []
	genotypes =[]
	matrix = [[],[],[]]
	max = 0
	# Set up temporary files for data to be pushed into 
	with tempfile.NamedTemporaryFile() as vcf:
		try:
			fh = open(vcf_file_name, 'r')
			#fh = zipfile.ZipFile(fh)
			for line in fh:
				if '##' in line:
					pass
				elif '#' in line:
					samples = line.strip().split()[9:]
				else:
					VCF_parse_row(line,alleles,matrix)
					
		except IOError:
			print "Error: File does not seem to exist"

	return alleles
	# Find the total length of the genome sequences 
	# Samples there are in the file (max) 

	vcf.close()

def VCF_parse_row(line, alleles, matrix):
	row = -1
	line=line.strip('\n')
	line=line.split('\t')
	# Array of all of the reference alleles and alternative alleles
	alleles.append(line[3:5])
	# Finds max allele length in allele array 
	max_length = map(lambda allele: max(map(lambda x: len(x), allele)) ,alleles)

	for x in alleles:
		if int(len(x)) < max_length:
			x = x+('-'* int(max_length))
			print x

	# Start of matrix 
	counter =-1
	for i in line[9:]:
		row += 1
		i = i.split('|')
		for x in i:
			counter +=1
			if x == '0':
				pass
			elif x == '1':
				matrix[0].append(row)  # Rows
				matrix[1].append(counter) # Columns
				matrix[2].append(int(x))   # Values	
	#return alleles


# def phylip_format(sequences):
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 

print VCF_parser('input.txt')


