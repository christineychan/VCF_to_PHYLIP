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
	rows = 0
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
					rows +=1 
					VCF_parse_row(line,alleles,matrix,rows)
					
		except IOError:
			print "Error: File does not seem to exist"

	return matrix
	# Find the total length of the genome sequences 
	# Samples there are in the file (max) 

	vcf.close()

def VCF_parse_row(line, alleles, matrix, rows):
	line=line.strip('\n')
	line=line.split('\t')
	# Array of all of the reference alleles and alternative alleles
	alleles.append(line[3:5])
	# Finds max allele length in allele array 
	for allele in alleles:
		max_length = max(map(lambda a: len(a),allele))

	for a in range(len(allele)):
		if int(len(allele[a])) < max_length:
			allele[a] = allele[a]+('-'* int(max_length-int(len(allele[a]))))

	# Start of matrix 
	columns = 0
	for i in line[9:]:
		i = i.split('|')
		for x in i:
			if x == '0':
				pass
			elif x == '1':
				matrix[0].append(rows)    # Rows
				matrix[1].append(columns) # Columns
				matrix[2].append(int(x))  # Values	
			columns +=1
	#return alleles

# def phylip_format(sequences):
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 

print VCF_parser('input.txt')


