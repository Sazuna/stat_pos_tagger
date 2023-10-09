#!/bin/python3

import pandas
import json

with open("../freqmotspos.json", 'r') as f:
	string = f.read()
	freqmotspos = json.loads(string)	

#matrice

df_toks_pos = pandas.DataFrame.from_dict(freqmotspos)


df_toks_pos = df_toks_pos.fillna(0) # transforme tous les NaN en 0.
#df_toks_pos += 1 # rajoute 1 partout où ce n'est pas NaN.

df_toks_pos = df_toks_pos.T
df_pos = df_toks_pos.sum()


#Matrice de génératins p_gen
p_gen = df_toks_pos / df_pos

with open("../freqpospos.json", 'r') as f:
	string = f.read()
	freqpospos = json.loads(string)
df_pos_pos = pandas.DataFrame.from_dict(freqpospos)

df_pos_pos = df_pos_pos.fillna(0)
df_pos_pos = df_pos_pos

p_trans = df_pos_pos / df_pos_pos.sum()

# quelle est la probabilité de cette phrase si on a les POS suivants ?
phrase = "le président gagne"
pos = "DET NOUN VERB"

tok_lst = phrase.split(' ')
pos_lst = pos.split(' ')
prevpos = '_'
proba_sent = 1
for tok, pos in zip (tok_lst, pos_lst):
	p_gen_ = p_gen[pos][tok]
	p_trans_ = p_trans[prevpos][pos]#[prevpos][pos]
	proba_sent *= p_gen_ * p_trans_
	print(p_gen_, p_trans_, proba_sent)
	prevpos = pos

print("proba sent:", proba_sent)
