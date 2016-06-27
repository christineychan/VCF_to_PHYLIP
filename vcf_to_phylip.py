# This python script coverts vcf files into phylip format

# Modules 
from scipy.sparse import coo_matrix 
from sys import argv
import tempfile 

# Set up temporary files for data to be pushed into 
with tempfile.NamedTemporaryFile() as temp:
	temp.name: vcf

def VCF_parser(vcf_file_name)
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
		# Parse the row for genotypes 
		else:
			genotypes = line.strip()split()[9:]
			for i in genotypes:
				i = i.replace("|", "")

	# Make an array of all of the reference alleles (in row 3)
	# Make an array of all of the alternative alleles (in row 4)

	# Make an array for the genotypes

def VCF_parse_row(row, samples)
	# Take the 9th column+ and make an array called "Sample_Names"
	# Figure out how many samples there are in the file (max) 
	# Find the total length of the genome sequences 

def phylip_format(sequences)
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 




