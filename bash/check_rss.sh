#!/bin/bash

total=$(ps -A o pid,rss:8,user,cmd|awk 'NR>1 {A+=$2} END{print A}')
output="OK - all users $total|all_users=$total"

if [ "$#" -eq 1 ]; then
    user=$1
    rss=$(ps -u $user o pid,rss:8,cmd | awk 'NR>1 {A+=$2} END{print A}')
    output="OK - $user user $rss, all users $total|all_users=$total;;; $user=$rss"
fi

echo $output
