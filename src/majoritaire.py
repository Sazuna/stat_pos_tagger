#!/bin/python3

from collections import defaultdict
import json


freqmots = defaultdict(int)
freqpos = defaultdict(int)
freqmotspos = defaultdict(lambda: defaultdict(int))
freqposmots = defaultdict(lambda: defaultdict(int))

for line in open('GDN_POS_1000.txt'):
	tokspos = line.split(' ')
	for tokpos in tokspos:
		tokposlst = tokpos.split('/')
		if len(tokposlst) == 2:
			token, pos = tokposlst
			# print(token, pos)
			freqmots[token] += 1
			freqpos[pos] += 1
			freqmotspos[token][pos] += 1
			freqposmots[pos][token] += 1

"""
print(freqmots)
print(freqmotspos)
print(freqmotspos['la'])
"""
print(freqposmots['VERB'])


def tag(corpus):
	for token in corpus.split(' '):
		freqs = freqmotspos[token]
		if freqs:
			pos = max(freqs, key=freqs.get)
			print(token + '/' + pos, end=' ')
		else:
			pos = max(freqpos, key=freqpos.get)	
			print("pas dans le dic: " + token + '/' + pos, end=' ')

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

tag("Je ne veux pas me lever .")
