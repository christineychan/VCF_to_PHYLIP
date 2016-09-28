#!/usr/bin/python

in_file = "input.txt"

fh = open(in_file, "r")

samples = []
ref = []
alt = []
genotypes=[]

for line in fh:
    if '##' in line:
        pass
    elif '#' in line:
        samples = line.strip().split()[9:]
    else:
        line=line.strip('\n')
        line=line.split('\t')
        genotypes.extend(line[9:])
        ref.extend(line[3:4])
        alt.extend(line[4:5])
        
print ref
print alt
print samples
print genotypes
        
fh.close()
