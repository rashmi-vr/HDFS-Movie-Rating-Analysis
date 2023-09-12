#!/usr/bin/env bash

cat r5.txt | ./mapper.py > mapout5.txt
cat mapout5.txt | ./combiner.py > comout5.txt 
sort comout5.txt | ./reducer.py > results5.txt