# This python script coverts vcf files into phylip format

from sys import argv
import tempfile 
import gzip 

# Main Function 
def VCF_parser(vcf_file_name):
	sample_count = 0
	# Set up temporary files for data to be pushed into 
	with tempfile.NamedTemporaryFile() as vcf:
		try:
			vcf = gzip.open(vcf_file_name, 'r') 
			return VCF_data(vcf) 
		except IOError:
			print "Error: File does not seem to exist"
			 
	# Array of all of the reference alleles and alternative alleles
	refAlleles = ",".join(line[3:])
	altAlleles = ",".join(line[4:])
	# Parse the row for genotypes
	genotypes = line.strip().split()[9:]

	for i in genotypes:
			i = i.replace("|", "")
	# Samples there are in the file (max) 
	return sample_count 
	# Find the total length of the genome sequences 
	return len(sequence)

	vcf.close()

def VCF_data(vcf):
	for line in vcf:
		# Take the VCF file and skip over metadata (lines start with '##')
		if line.startswith('##'):
			pass 
		# Identify the sample names and VCF headers if the line starts with '#'
		elif line.startswith('#'):
			samples = line.split()[9:]
			for i in samples:
				sequence[i] = ""
				sample_count += 1 

def VCF_parse_row(matrix, alleles, genotypes):
	# Make a sparse matrix row for the genotypes for each sample
		# Create a matrix that adjusts the parameters (sequence length and sample)
	# Replace '1' in sparse matrix row with ALT alleles 
	# Include REF alleles within the sequence 
	return false
	
# def phylip_format(sequences):
	# Create a dictionary and push information 
	# Print sample name 
	# Print sequence 

# Create an if statement that executes both functions and then closes 
# the temporary files 




