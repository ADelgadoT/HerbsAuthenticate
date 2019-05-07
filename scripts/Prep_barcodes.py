### Prep_Barcodes.py generates KMA command to execute barcodes extraction through KMA. 

def prep_barcodes(path_forward_reads, path_reverse_reads, sample_name, kma_barcodes_model, kma_path, db_path, out_path):

    #Extract data from input file and create script: 
    kma_script = open(kma_barcodes_model, 'r')
    #out_file = open(sample_name+'_kma_Mapping.sh', 'w')
    
    #Read kma file and modify the kma command: 
    for line in kma_script: 
        tmp_line = line.replace('path_R1', path_forward_reads)
        tmp_line2 = tmp_line.replace('path_R2', path_reverse_reads)
        tmp_line3 = tmp_line2.replace('sample_name', sample_name)
        tmp_line4 = tmp_line3.replace('kma_dir', kma_path)
        tmp_line5 = tmp_line4.replace('out_dir', out_path)
        final = tmp_line5.replace('database_backbone', db_path)
    
    #Close output file: 
    #out_file.close()
    kma_script.close()

    return final

def blast_id_extraction(blast_file):
    import pandas as pd
    blastn_results = pd.read_table(blast_file, header = None)

    blastn = blastn_results.iloc[:,[0,1]].drop_duplicates()

    label = blastn.iloc[:,1]
    id_fasta = blastn.iloc[:,0]
    id_tax = list()

    for individual_label in label: 
        columns = individual_label.split('|')
        id_tax.append(columns[3])
    
    return (id_fasta,id_tax)

def tax_extraction(blast_id):
    import subprocess
    
    fh = blast_id
    output_id=list()
    specie_id=list()

    for line in fh:
        line = line.rstrip()
        cmd = '/home/databases/metagenomics/scripts/get_kch.pl -i "%s" -d /home/databases/metagenomics/db/nt/nt.kch -I' % line
        
        proc = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
        raw_result = proc.stdout.read().decode('utf-8')    
        col = raw_result.split("\t")        

        #Extract tax ID and specie:
        output_id.append(col[0])
        specie_id.append(col[13])	

    return (output_id, specie_id)

def header_std(fasta_file, specie_name, total_barcodes, output_dir, valid_id):
    
	#Import data and variables: 
	input_file = open(fasta_file, 'r')
	output_file = open(output_dir + '/' + specie_name + '_Final_Barcodes.fsa', 'w')
	specie = specie_name
	total_number_barcodes = str(total_barcodes)
	id_name = ''
	valid_id = list(valid_id)

	#Iterate over the fasta file:
	for line in input_file:

	        #Check if it is a header or not:
		if line[0] == '>':

			#Extract header and validate:
			id_name = line[1:-1]
			
			if id_name not in valid_id:
				id_name = ''
			
			else:
				#Std header and write it in the output:
				col = line.split("_")
				header = col[0] + '|' + specie + '|' + col[1][:-1] + '|' + total_number_barcodes
				print(header, file=output_file)
				
		else:
			if id_name != '':
				print(line[:-1], file=output_file)

	input_file.close()
	output_file.close()
