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
with open("freqbigramspos.json", 'r') as f:
	string = f.read()
	freqbigramspos = json.loads(string)

def majoritaire(corpus):
	res = ""
	for token in corpus.split(' '):
		if token in freqmotspos:
			freqs = freqmotspos[token]
			#if freqs:
			pos = max(freqs, key=freqs.get)
			res += token + '/' + pos + ' '
		else:
			pos = max(freqpos, key=freqpos.get)	
			res += token + '/' + pos + ' '
	return res

def bigrams(corpus):
	res = ""
	prevtok = '_'
	for token in corpus.split(' '):
		bigram = prevtok + '-' + token
		if bigram in freqbigramspos:
			#motsposmax = max(freqbigramspos[bigram].items(), key = labmbda i:i[1])
			#res += token + '/' + motsposmax[0] + ' '
			freqs = freqbigramspos[bigram]
			pos = max(freqs, key=freqs.get)
			res += token + '/' + pos + ' '
		elif token in freqmotspos:
			#motsposmax = max(freqmotspos[token].items(), key = lambda i:i[1])
			#res += token + '/' + motsposmax[0]
			freqs = freqmotspos[token]
			pos = max(freqs, key=freqs.get)
			res += token + '/' + pos + ' '
		else:
			pos = max(freqpos, key=freqpos.get)	
			res += token + '/' + pos + ' '
	return res

def main(corpus, method):
	if method == 'majoritaire':
		print(majoritaire(corpus))
	elif method == 'bigrams':
		print(bigrams(corpus))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Tags a corpus already tokenized on spaces.')
	parser.add_argument('-m', '--method', type=str, required=True, help='Method to use to pos tag corpus.')
	args = parser.parse_args()

	corpus = sys.stdin.read().strip()
	main(corpus, args.method)
