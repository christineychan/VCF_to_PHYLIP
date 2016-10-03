#!/usr/bin/python

import zipfile
import tempfile

# Main Function 
def vcf_parser(vcf_file_name):
	samples = []
	ref = []
	alt = []
	genotypes =[]

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
                    # Parse the row for genotypes
					genotypes.append(line[9:])
                    # Array of all of the reference alleles and alternative alleles
					ref.extend(line[3:4])
					alt.extend(line[4:5])
					# Parse the row for genotypes
					genotypes.append(line[9:])
		except IOError:
			print "Error: File does not seem to exist"

	for g in genotypes:
		for x in g:
			x = x.replace("|",",")
			
	#for i in genotypes:
			#i = i.replace("|", "")
	# Samples there are in the file (max) 
	return genotypes
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



