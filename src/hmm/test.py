#!/bin/python3

import pandas
import json

with open("../freqmotspos.json", 'r') as f:
	string = f.read()
	freqmotspos = json.loads(string)	

#matrice

df_toks_pos = pandas.DataFrame.from_dict(freqmotspos)
print(df_toks_pos)
print(df_toks_pos['de'].sum())
print(df_toks_pos['de']['VERB'])
print(df_toks_pos['de'].idxmax())
print(df_toks_pos.columns)
print(df_toks_pos.index)

print(df_toks_pos.sum().sum()) # nombre de mots dans le corpus d'apprentissage
# c'est supposé faire 27.680


df_toks_pos = df_toks_pos.fillna(0) # transforme tous les NaN en 0.
#df_toks_pos += 1 # rajoute 1 partout où ce n'est pas NaN.
print(df_toks_pos)
print(df_toks_pos['de'].sum())
print(df_toks_pos['de']['VERB'])
print(df_toks_pos['de'].idxmax())
print(df_toks_pos.columns)
print(df_toks_pos.index)

print(df_toks_pos.sum().sum()) # nombre de mots dans le corpus d'apprentissage

df_toks_pos = df_toks_pos.T
df_pos = df_toks_pos.sum()
print(df_pos)


#Matrice de génératins p_gen
p_gen = df_toks_pos / df_pos
print("P GEN:::::::")
print(p_gen)
print(p_gen['DET'])

with open("../freqpospos.json", 'r') as f:
	string = f.read()
	freqpospos = json.loads(string)
print(freqpospos)
df_pos_pos = pandas.DataFrame.from_dict(freqpospos)

df_pos_pos = df_pos_pos.fillna(0)
df_pos_pos = df_pos_pos.T

print(df_pos_pos)
p_trans = df_pos_pos / df_pos_pos.sum()

print(p_trans)



# quelle est la probabilité de cette phrase si on a les POS suivants ?
phrase = "Le président gagne ."
pos = "DET NOUN VERB PUNCT"

tok_lst = phrase.split(' ')
pos_lst = pos.split(' ')
prevpos = '_'
proba_sent = 1
for tok, pos in zip (tok_lst, pos_lst):
	print(tok, pos)	
	print(p_gen)
	p_gen_ = p_gen[pos][tok]
	p_trans_ = p_trans[pos][prevpos]#[prevpos][pos]
	proba_sent *= p_gen_ * p_trans_
	prevpos = pos

print("proba sent:", proba_sent)
