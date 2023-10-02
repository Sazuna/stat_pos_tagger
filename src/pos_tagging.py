#!/bin/python3

import json
import sys
import argparse

with open("freqmots.json", 'r') as f:
	string = f.read()
	freqmots = json.loads(string)

with open("freqpos.json", 'r') as f:
	string = f.read()
	freqpos = json.loads(string)

with open("freqposmots.json", 'r') as f:
	string = f.read()
	freqposmots = json.loads(string)

with open("freqmotspos.json", 'r') as f:
	string = f.read()
	freqmotspos = json.loads(string)

def majoritaire(corpus):
	for token in corpus.split(' '):
		if token in freqmotspos:
			freqs = freqmotspos[token]
			#if freqs:
			pos = max(freqs, key=freqs.get)
			print(token + '/' + pos, end=' ')
		else:
			pos = max(freqpos, key=freqpos.get)	
			print(token + '/' + pos, end=' ')

def main(corpus, method):
	if method == 'majoritaire':
		majoritaire(corpus)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Tags a corpus already tokenized on spaces.')
	parser.add_argument('-m', '--method', type=str, required=True, help='Method to use to pos tag corpus.')
	args = parser.parse_args()

	corpus = sys.stdin.read().strip()
	main(corpus, args.method)
