import spacy
nlp = spacy.load("fr_dep_news_trf")

import sys
for line in sys.stdin:
	print(line)
	doc = nlp(line.strip())
	tokspos = ''
	for token in doc:
		tokspos += token.text+'/'+token.pos_+' '
	print(tokspos)
