#!/bin/bash

cpu_array=($(iostat -y -c 1 2 | tail -2 | head -1))

us=${cpu_array[0]}
ni=${cpu_array[1]}
sy=${cpu_array[2]}
io=${cpu_array[3]}
st=${cpu_array[4]}
id=${cpu_array[5]}

output="OK - cpu iowait $io% |iowait=$io%"

if [ "$#" -eq 1 ]; then
    disk=$1
    util=$(iostat -x -y -p $disk 1 2 | grep -P "$disk\b" | tail -1 | awk 'END{print $NF}')
    output+=";;; $disk=$util%"
fi

echo $output
