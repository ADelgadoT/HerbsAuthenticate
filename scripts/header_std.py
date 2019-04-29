### Function to std headers from obtained barcodes fasta file: 

def header_std(fasta_file, specie_name, total_barcodes, output_dir)
	
	#Import data and variables: 
	input_file = open(fasta_file, 'r')
	output_file = open(output_dir + '/' + specie_name + '_Final_Barcodes.fsa', 'w')
	specie = specie_name
	total_number_barcodes = str(total_barcodes)

	for line in input_file: 
    if line[0] == '>':
        col = line.split("_")
        header = col[0] + '|' + specie + '|' + col[1][:-1] + '|' + total_number_barcodes
        print(header, file=output_file)
    else:
        print(line[:-1], file=output_file)

	input_file.close()
	output_file.close()
