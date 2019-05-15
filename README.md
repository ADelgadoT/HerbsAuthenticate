# HerbsAuthenticate

The HerbsAuthenticate package process trimmed FASTQ files from both single or paired-end reads to perform sequence mapping against barcode databases. Additionally, it is also able to build customized databases based on the user’s needs by extracting specific barcodes from the trimmed reads.

## Requirements and instalation
The script requires **Python3** and the following programs to be installed:
- KMA 
- blastn 

To install the package, download the directory. Check the `config.yaml` file and make sure that all the paths to the executables are absolute and indeed refer to a working executable.

## Indexing
Before aligning reads with KMA, the database must be indexed. This is done with the following command: 

`kma index -i path_to_database.fasta -o output_directory` 

The default k-mer size is 16. In case you want to change it, please add the option `-k` followed by the desired k-mer size. 

## Extract barcodes
The script `Barcodes.py` is used to obtain the barcodes from the trimmed reads. In order to execute it, please follow the steps indicated below: 

1. Create an input file, using `input.txt` as an example. It is a space-separated file in which each line represents the data from one sample. There are three columns: 
    - Column 1: absolute path to forward reads
    - Column 2: absolute path to reverse reads
    - Column 3: scientic sample name (Binomial nomenclature)
   
2. Ensure that `config.yaml` is located in the same directory as `Barcodes.py` and the `scripts` folder. 
3. Update `config.yaml` parameters according to your data and type of analysis you want to perform. The options available are shown below:

    **Path**:
      - kma: Absolute path to KMA directory.
      - db_backbone: Absolute path to indexed backbone barcode database.
      - output: Absolute path to output directory. 

    **Validation**:
      - merge_by_genus: boolean variable that indicates whether the validation
is at genus or specie level. Default value: TRUE.

4. Excute the following command: `python3 Barcodes.py input.txt`

## Mapping
To map trimmed reads against a specific barcode database, the script `Mapping.py` is used. In order to execute it, please follow the steps indicated below: 

1. Create an input file, using `input.txt` as an example. It is a space-separated file in which each line represents the data from one sample. There are three columns: 
    - Column 1: absolute path to forward reads
    - Column 2: absolute path to reverse reads
    - Column 3: sample name 
   
2. Ensure that `config.yaml` is located in the same directory as `Mapping.py` and the `scripts` folder. 
3. Update `config.yaml` parameters according to your data and type of analysis you want to perform. The options available are shown below:

    **Path**:
      - kma: Absolute path to KMA directory.
      - db: Absolute path to indexed database.
      - output: Absolute path to output directory. 
               
    **Reads**:
      - PE/SE: Pair-ended (PE) or single-ended (SE) reads.

    **Mapping**:
      - merge_by_genus: boolean variable that indicates whether the identification
is at genus or specie level. Default value: TRUE. 
      - min_barcodes: Minimum number of identitifed barcodes from a genus or specie to be considered as a true positive. Default value: 2.

4. Excute the following command: `python3 Mapping.py input.txt`

## For Computerome users
In case you are executing any of these scripts in Computerome: 
1. Save either `python3 Barcodes.py input.txt` or `python3 Mapping.py input.txt` in a text file named `run_HerbsAuthenticate_qsub.sh`

2. Execute the following command: 

`qsub -W group_list=your_group -A your_group -l nodes=1:ppn=4,mem=50gb,walltime=1:00:00:00 -d path/to/your/output/directory run_HerbsAuthenticate_qsub.sh`
