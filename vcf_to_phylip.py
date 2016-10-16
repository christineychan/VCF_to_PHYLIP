#!/usr/bin/python

import zipfile
import tempfile


# Main Function 
def VCF_parser(vcf_file_name):
	samples = []
	ref = []
	alt = []
	genotypes =[]
	matrix = [[],[],[]]
	alleles = []
	counter = -1
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
					line=line.strip('\n')
					line=line.split('\t')
                    # Array of all of the reference alleles and alternative alleles
					ref = ''.join(line[3:4])
					alt = ''.join(line[4:5])
					# Calculate maximum allele length 
					if len(ref) < len(alt):
						ref = ref + "-" * (len(alt)-1)
					else:
						alt = alt + "-" * (len(ref)-1)
					# Start of matrix 
					counter +=1
					counter2 =-1
					for i in line[9:]:
						i = i.split('|')
						for x in i:
							counter2 +=1
							if x == '0':
								pass
							elif x == '1':
								matrix[0].append(counter)  # Rows
								matrix[1].append(counter2) # Columns
								matrix[2].append(int(x))   # Values	
		except IOError:
			print "Error: File does not seem to exist"

	return matrix
	# Find the total length of the genome sequences 
	# Samples there are in the file (max) 

	vcf.close()

#def VCF_parse_row(matrix, alleles, genotypes):
	# Make a sparse matrix row for the genotypes for each sample
		# Create a matrix that adjusts the parameters (sequence length and sample)
		
	# Replace '1' in sparse matrix row with ALT alleles 
	# Include REF alleles within the sequence 
	#return false


# def phylip_format(sequences):
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 

print VCF_parser('input.txt')


