#!/bin/python3

from collections import defaultdict
import json
import argparse


def learn_from(document):
	freqmots = defaultdict(int)
	freqpos = defaultdict(int)
	freqmotspos = defaultdict(lambda: defaultdict(int))
	freqposmots = defaultdict(lambda: defaultdict(int))
	freqbigramspos = defaultdict(lambda: defaultdict(lambda: defaultdict(int))) 
	for line in open(document, 'r'):
		tokspos = line.split(' ')
		prevtoken = '_'
		for tokpos in tokspos:
			tokposlst = tokpos.split('/')
			if len(tokposlst) == 2:
				token, pos = tokposlst
				# print(token, pos)
				freqmots[token] += 1
				freqpos[pos] += 1
				freqmotspos[token][pos] += 1
				freqposmots[pos][token] += 1
				freqbigramspos[prevtoken][token][pos] += 1
				prevtoken = token

	"""
	print(freqmots)
	print(freqmotspos)
	print(freqmotspos['la'])
	"""
	print(freqposmots['VERB'])


	json_obj = json.dumps(freqmots, indent=3)
	with open("freqmots.json", 'w') as f:
		f.write(json_obj)

	json_obj = json.dumps(freqpos, indent=3)
	with open("freqpos.json", 'w') as f:
		f.write(json_obj)

	json_obj = json.dumps(freqmotspos, indent=3)
	with open("freqmotspos.json", 'w') as f:
		f.write(json_obj)
		
	json_obj = json.dumps(freqposmots, indent=3)
	with open("freqposmots.json", 'w') as f:
		f.write(json_obj)

	json_obj = json.dumps(freqbigramspos, indent=3)
	with open("freqbigramspos.json", 'w') as f:
		f.write(json_obj)

	# Test maj
	def tag(corpus):
		for token in corpus.split(' '):
			freqs = freqmotspos[token]
			if freqs:
				pos = max(freqs, key=freqs.get)
				print(token + '/' + pos, end=' ')
			else:
				pos = max(freqpos, key=freqpos.get)	
				print("pas dans le dic: " + token + '/' + pos, end=' ')

	tag("Je ne veux pas me lever .")

def main(document):
	learn_from(document)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Creates json files from a POS-tagged corpus.')
	parser.add_argument('-c', '--corpus', type=str, required=True, help='Corpus. Format: TOKEN/POS separated with spaces.')	

	args = parser.parse_args()
	main(args.corpus)
