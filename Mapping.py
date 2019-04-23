#!/usr/bin/env python3

## PARSER for executing all scripts needed for the mapping procedure. 

##Import all required libraries and input data: 
#Load libraries: 
import sys
import subprocess

#Update path:
sys.path.insert(0, "./scripts")
import Mapping_Results_Processing
import Prep_Barcode_Generation_BM

##Initialize loop for all samples in input file: 
sample_data = open(sys.argv[1], 'r')

for line in sample_data:
	col = line.split()

	##Count total sample reads: 
	s = subprocess.check_output(["./scripts/count_reads.sh","PE", col[0], col[1]]) 
	print(int(s))
	
	##Prepare kma script and execute it: 
	kma = Prep_Barcode_Generation_BM.prep_kma(col[0], col[1], col[2], "./scripts/mapping_model.sh")

	execute_kma = subprocess.Popen(kma, shell=True)
	execute_kma.communicate()
