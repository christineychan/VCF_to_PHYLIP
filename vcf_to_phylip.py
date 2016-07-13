# This python script coverts vcf files into phylip format

from scipy.sparse import coo_matrix 
from sys import argv
import tempfile 

# Set up temporary files for data to be pushed into 
with tempfile.NamedTemporaryFile() as temp:
	temp.name: vcf

def VCF_parser(vcf_file_name)
	sample_count = 0
	# Obtain and open VCF file 
	vcf = open(vcf_file_name, 'r')
	# Take the VCF file and skip over the metadata (lines start with '##')
	for line in vcf:
		if line.startswith('##'):
			pass 
	# Take the VCF file and skip over metadata (lines start with '#')
		elif line.startswith('#'):
		# Identify the sample names and VCF headers if the line starts with '#'
			samples = line.split()[9:]
			for i in samples:
				sequence[i] = ""
				sample_count += 1 
		# Parse the row for genotypes 
		else:
		# Array of all of the reference alleles and alternative alleles
			alleles = ",".join(line[3:4])

	# Samples there are in the file (max) 
	return sample_count 
	# Find the total length of the genome sequences 
	return len(sequence)

def VCF_parse_row(row, samples)
	# Make an array for the genotypes
	genotypes = line.strip().split()[9:]
			for i in genotypes:
				i = i.replace("|", "")
	# Make a sparse matrix with coo_matrix 
	
def phylip_format(sequences)
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 




