### Prep_Barcode_Generation_BM.py generates all kma scripts to generate their barcodes. They will also output the execution time for benchmarking purposes

#Import required libraries
import sys

#Open input file with sample data: 
sample_file = open(sys.argv[1],'r')
 
#Extract data from input file and create script: 
for line in sample_file:
    kma_script = open(sys.argv[2], 'r')
    columns = line.split()
    out_file = open(columns[2]+'_kma_Mapping.sh', 'w')
    
    #Read kma file and modify the kma command: 
    for line in kma_script: 
        tmp_line = line.replace('path_R1', columns[0])
        tmp_line2 = tmp_line.replace('path_R2', columns[1])
        tmp_line3 = tmp_line2.replace('sample_name', columns[2])
        print(tmp_line3, file = out_file)
    
    #Close output file: 
    out_file.close()
    kma_script.close()

#Close inputs file: 
sample_file.close()
