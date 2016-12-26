#!/usr/bin/python

import zipfile
import tempfile

# Main Function 
def vcf_parser(vcf_file_name):
	samples = []
	alleles = []
	matrix = [[],[],[]]
	sequence = ()
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
					vcf_parse_row(line,alleles,matrix,rows)
					rows +=1 
					
		except IOError:
			print "Error: File does not seem to exist"
	
	sortedcol = parse_matrix(alleles,matrix)
	sequence = []
	temp = []

	# Parses through the sparse matrix 

	for i in range(len(sortedcol)):
		column = sortedcol[i]
		temp.append('\n')

		# Adds any skipped columns 
		if i not in matrix[1]:
			for row in range(len(alleles)):
				temp.append(alleles[row][0])
		else:

			# Adds any skipped rows 
			for row in range(len(alleles)):
				if row != matrix[0][column]:
					temp.append(alleles[row][0])
				else:
					# Work on this line, with double columns in column array 
					if matrix[1].count(i) > 1:
						temp.append(alleles[matrix[0][column]][1])

					# Adds the correct alternative allele for row and column 
					else:
						temp.append(alleles[matrix[0][column]][matrix[2][column]])
	sequence = ''.join(temp)

	print sequence

	# Find the total length of the genome sequences 
	# Samples there are in the file (max) 

	vcf.close()

def vcf_parse_row(line, alleles, matrix, rows):
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

def parse_matrix(alleles, matrix):

	# Returns the index of the original column array in sorted order 
	return [i[0] for i in sorted(enumerate(matrix[1]), key=lambda x:x[1])]
	

# def phylip_format(sequences):
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 

print vcf_parser('input.txt')


