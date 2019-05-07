#!/usr/bin/env python3

## PARSER for executing all scripts needed for extracting all barcodes. 

##Import all required libraries and input data: 
#Load libraries: 
import sys
import subprocess
import yaml
import pandas as pd

#Update path and import scripts:
sys.path.insert(0, "./scripts")
import Prep_barcodes


#Read config file and parse variables:
with open("config.yaml", "r") as ymlfile:
	cfg = yaml.load(ymlfile)

kma_path = cfg["path"].get("kma")
output_dir = cfg["path"].get("output")
db_path = cfg["path"].get("db_backbone")
validation_factor = cfg["validation"].get("merge_by_genus")

##Initialize loop for all samples in input file: 
sample_data = open(sys.argv[1], 'r')

for line in sample_data:
	col = line.split()

	##Prepare kma script and execute it: 
	kma = Prep_barcodes.prep_barcodes(col[0], col[1], col[2], "./scripts/barcodes_model.sh", kma_path, db_path, output_dir)
	print("Executing KMA" + col[2])
	execute_kma = subprocess.Popen(kma, shell=True)
	execute_kma.communicate()

	##Blastn validation
	query_file = output_dir + '/' + col[2] + '_Barcodes.fsa'
	blast = 'blastn -query ' + query_file + ' -db /home/databases/metagenomics/db/nt/nt -evalue 0.0001 -out ' + query_file + '.blastnt -outfmt 6 -max_target_seqs 1'
	print("Executing Blastn")
	execute_blastn = subprocess.Popen(blast, shell=True)
	execute_blastn.communicate()

	blast_result = query_file + '.blastnt'
	id_fasta, id_tax_1 = Prep_barcodes.blast_id_extraction(blast_result)
	id_tax_2, specie = Prep_barcodes.tax_extraction(id_tax_1)

	#Correct specie: 
	if validation_factor:
		columns = col[2].split('_')
		correct_specie = columns[0]
	else:
		correct_specie = col[2].replace('_', ' ')	

	#Binary validation: 
	print("Validation in process")
	binary_validation = list()
	for individual_specie in specie:
		if validation_factor:
			get_genus = individual_specie.split()
			individual_specie = get_genus[0]

		if individual_specie == correct_specie:
			binary_validation.append(1)
		else:
			binary_validation.append(0)

	#DataFrame creation with validation results and output it:
	validation = pd.DataFrame(list(zip(id_fasta, specie, binary_validation)), columns=['ID', 'Specie', 'Validation'])
	validation_output = output_dir + '/' + col[2] + '_Validation.txt'
	validation.to_csv(validation_output, sep = '\t')


	valid_id = list(validation.loc[validation['Validation'] == 1, 'ID'])
	total_barcodes = len(valid_id)
	
	#Final barcodes fasta file generation + header std:  
	Prep_barcodes.header_std(query_file, col[2], total_barcodes, output_dir, valid_id)

