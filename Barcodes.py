#!/usr/bin/env python3

## PARSER for executing all scripts needed for extracting all barcodes. 

##Import all required libraries and input data: 
#Load libraries: 
import sys
import subprocess
import yaml

#Update path and import scripts:
sys.path.insert(0, "./scripts")
import Prep_barcodes
import header_std

#Read config file and parse variables:
with open("config.yaml", "r") as ymlfile:
	cfg = yaml.load(ymlfile)

kma_path = cfg["path"].get("kma")
output_dir = cfg["path"].get("output")
db_path = cfg["path"].get("db_backbone")

##Initialize loop for all samples in input file: 
sample_data = open(sys.argv[1], 'r')

for line in sample_data:
	col = line.split()

	##Prepare kma script and execute it: 
	kma = Prep_barcodes.prep_barcodes(col[0], col[1], col[2], "./scripts/barcodes_model.sh", kma_path, db_path, output_dir)
	print(kma)
	#execute_kma = subprocess.Popen(kma, shell=True)
	#execute_kma.communicate()

	##Blastn validation
	query_file = output_dir + '/' + col[2] + '_Barcodes.fsa'
	blast = 'blastn -query ' + query_file + ' -db /home/databases/metagenomics/db/nt/nt -evalue 0.0001 -out ' + query_file + '.blastnt -outfmt 6 -max_target_seqs 1'
	print(blast)

	execute_blastn = subprocess.Popen(blast, shell=True)
	execute_blastn.communicate()

	##Header standardization: 
	#header_std.header_std(fasta_file, specie_name, total_barcodes, output_dir)
