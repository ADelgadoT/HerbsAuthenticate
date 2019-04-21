#!/bin/sh

#Help message? - yes or no? 

#Read parameters from command line: 
read_pair = $1
file = $2

#Check if file exists and proceed if it does: 
if test -f "$FILE"; then

	case read_pair in:

		#Paired-end reads:
		"PE") 
			reads = wc -l $2
			total_reads = reads*2

		#Single-end reads:
		"SE")
			total_reads = wc -l $2

		#Display help message:
		"-h")
			echo $usage

		#Error message: 
		*)
			echo "Please introduce a valid option (PE/SE). For more information, use -h option."
	esac

else
	echo "Please introduce a valid file path to your trimmed reads."

return total_reads
