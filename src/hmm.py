from collections import defaultdict
import json
freqmots = defaultdict(int)
freqpos = defaultdict(int)
freqmotspos = defaultdict(lambda: defaultdict(int))
freqpospos = defaultdict(lambda: defaultdict(int))

"""
for line in open('GDN_POS_train.txt'):
	tokspos = line.split(' ')
	prevtok = '_'
	prevpos = '_'
	for tokpos in tokspos:
		tokposlst = tokpos.split('/')
		if len(tokposlst) == 2:
			token, pos = tokposlst
			# print(token, pos)
			freqmots[token] += 1
			freqpos[pos] += 1
			freqmotspos[token][pos] += 1
			freqpospos[prevpos][pos] += 1
			prevtok = token
			prevpos = pos
"""
with open("freqmotspos.json", 'r') as f:
	string = f.read()
	freqmotspos = json.loads(string)
with open("freqpospos.json", 'r') as f:
	string = f.read()
	freqpospos = json.loads(string)

with open("freqpos.json", 'r') as f:
	string = f.read()
	freqpos = json.loads(string)

pos_lst = freqpos.keys()

import pandas

df_toks_pos = pandas.DataFrame.from_dict(freqmotspos).T
df_toks_pos = df_toks_pos.fillna(0)
df_toks_pos += 1
p_gen = df_toks_pos/df_toks_pos.sum()

p_gen_unk = pandas.DataFrame.from_dict(df_toks_pos.sum()/df_toks_pos.sum().sum())

df_pos_pos = pandas.DataFrame.from_dict(freqpospos)
df_pos_pos = df_pos_pos.fillna(0)
df_pos_pos += 0
p_trans = df_pos_pos/df_pos_pos.sum()

import sys
for line in sys.stdin:
	tokspos = []
	tok_seq = line.split()
	sent_hyps = ((['_'], 1),)
	for tok in tok_seq:
		sent_hyps_new = ()
		for pos in pos_lst:
			pos_seq_best = None
			proba_best = 0
			for (pos_seq, proba_seq) in sent_hyps:
				pos_prev = pos_seq[-1]
				if tok in p_gen[pos]:
					proba_gen = p_gen[pos][tok]
				else:
					proba_gen = p_gen_unk[0][pos]
				proba_trans = p_trans[pos_prev][pos]
				proba = proba_seq*proba_gen*proba_trans
				# print(tok, pos)
				# print('gen', pos, tok, proba_gen)
				# print('trans', pos_prev, pos, proba_trans)
				# print('sent', proba)
				if proba >= proba_best:
					pos_seq_best = pos_seq+[pos]
					proba_best = proba
			sent_hyps_new += ((pos_seq_best, proba_best),)
		# print(tok)
		# print(sent_hyps_new)
		sent_hyps = sent_hyps_new
	sent_hyp_max = max(sent_hyps, key=lambda h:h[1])
	# print(tok_seq, sent_hyp_max[0])
	for tok, pos in zip (tok_seq, sent_hyp_max[0][1:]):
		tokspos.append(tok+'/'+pos)
	print(' '.join(tokspos))
