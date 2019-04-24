# HerbsAuthenticate

The HerbsAuthenticate package process trimmed FASTQ files from both single or paired-end reads to perform sequence mapping against barcode databases. Additionally, it is also able to build customized databases based on the user’s needs by extracting specific barcodes from the trimmed reads.

## Requirements and instalation:
The script requires **Python3** and the following programs to be installed:
- KMA 
- blastn 

To install the package, download the directory. Check the `config.yaml` file and make sure that all the paths to the executables are absolute and indeed refer to a working executable.

## Indexing: 

## Extract barcodes:

## Mapping:
To map trimmed reads against a specific barcode database, the script `Mapping.py` is used. In order to execute it, please follow the steps indicated below: 

1. Create an input file, using `input.txt` as an example. It is a space-separated file in which each line represents the data from one sample. There are three columns: 
    - Column 1: absolute path to forward reads
    - Column 2: absolute path to reverse reads
    - Column 3: sample name 
   
2. Ensure that `config.yaml` is located in the same directory as `Mapping.py` and the `scripts` folder. 
3. Update `config.yaml` parameters according to your data and type of analysis you want to perform. The options available are shown below:
    
4. Excute the script with the following command: 
`python3 Mapping.py input.txt`
