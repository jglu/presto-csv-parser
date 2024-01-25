#!/bin/bash

input_dir="./input"
input_files="${input_dir}/*.csv"

# parse all files in ${input_dir}

for file_name in ${input_files}
do
    # echo "filename is: ${file_name}"
    while read line
    do
        # awk -F ','
        echo "line is: ${line}"
    done < ${file_name}
done
