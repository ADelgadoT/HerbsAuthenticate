#!/bin/sh

#Help message? - yes or no? 
usage="Working on the help message." 

#Read parameters from command line: 
read_pair=$1
file=$2

#Check if file exists and proceed if it does: 
if test -f "$file"; then

	case $read_pair in

		#Paired-end reads:
		"PE")
			echo $(cat $file | wc -l)/2|bc
			;;

		#Single-end reads:
		"SE")
			echo $(cat $file | wc -l)/4|bc
			;;

		#Display help message:
		"-h")
			echo $usage
			exit 1
			;;

		#Error message: 
		*)
			echo "Please introduce a valid option (PE/SE). For more information, use -h option."
			exit 1
			;;
	esac

else
	echo "Please introduce a valid file path to your trimmed reads."

fi

