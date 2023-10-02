#!/bin/bash

FILE=$1

while read -r LINE
do
	LINE2=$(echo $LINE | sed -e 's/\/[A-Z]*//g')
	echo $LINE2 | ./pos_tagging.py -m majoritaire | ./eval.py $LINE
	#echo "Je ne veux pas me lever . " | ./pos_tagging.py -m majoritaire | ./eval.py Je/PRON ne/ADV veux/VERB pas/ADV me/PRON lever/VERB ./PUNCT
done < $FILE
