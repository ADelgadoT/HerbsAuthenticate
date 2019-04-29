#!/usr/bin/env python3

## PARSER for executing all scripts needed for the mapping procedure. 

##Import all required libraries and input data: 
#Load libraries: 
import sys
import subprocess
import yaml

#Update path and import scripts:
sys.path.insert(0, "./scripts")
import Mapping_Results_Processing
import Prep_KMA

#Read config file and parse variables:
with open("config.yaml", "r") as ymlfile:
	cfg = yaml.load(ymlfile)

config_reads = cfg["reads"].get("PE/SE")
kma_path = cfg["path"].get("kma")
output_dir = cfg["path"].get("output")
db_path = cfg["path"].get("db")
merge_by_genus = cfg["mapping"].get("merge_by_genus")
barcodes = cfg["mapping"].get("min_barcodes")

##Initialize loop for all samples in input file: 
sample_data = open(sys.argv[1], 'r')

for line in sample_data:
	col = line.split()

	##Count total sample reads: 
	s = subprocess.check_output(["./scripts/count_reads.sh", config_reads, col[0], col[1]]) 
	#print(int(s))
	
	##Prepare kma script and execute it: 
	kma = Prep_KMA.prep_kma(col[0], col[1], col[2], "./scripts/mapping_model.sh", kma_path, db_path, output_dir)
	
	execute_kma = subprocess.Popen(kma, shell=True)
	execute_kma.communicate()

	##Processing of the results: 
	mapstat = output_dir + "/" + col[2] + "_Mapping.mapstat"
	res = output_dir + "/" + col[2] + "_Mapping.res"

	Mapping_Results_Processing.map(mapstat, res, int(s), output_dir, col[2], merge_by_genus, barcodes)
