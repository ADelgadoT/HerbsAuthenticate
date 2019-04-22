#Start the timer: 
start=$(date +%s)

#Script: 
/home/projects/cge/analysis/plant_metagenomics/kma/kma -ipe path_R1 path_R2 -i path_R1 -t_db /home/projects/cge/data/plants_authenticity/IBol_Barcodes -mem_mode -1t1 -ef -t 4 -o /home/projects/cge/analysis/plant_metagenomics/test_kma/Mapping/sample_name_Mapping

#Stop the timer: 
end=$(date +%s)

#Process the time: 
diff=$(($end-$start))

echo " sample_name_Mapping_Executing time (s): $diff" > sample_name_Mapping_Time.txt
