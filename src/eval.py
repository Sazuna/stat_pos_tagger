#!/bin/python3
import sys
import pos_tagging as pt

def evaluation(predictions, labels):
	predlabels = list(zip(predictions.strip().split(' '), labels.strip().split(' ')))
	print(predlabels)
	errors = 0
	correct = 0
	#print(predlabels)
	for predlabel in predlabels:
		pred, label = predlabel[0].strip().split('/'), predlabel[1].strip().split('/')
		if pred[0] != label[0]:
			print(f"Test sentences and reference sentences are not identical. Diverging word: {pred[0]} and {label[0]}")
			sys.exit(1)
		else:
			if pred[1] == label[1]:
				correct += 1
			else:
				errors += 1
	print("correct :", correct)
	print("errors :", errors)
	print(f"precision : {correct / (correct + errors)}")

def evaluate(labels):
	sents = ' '.join([l.split('/')[0] for l in labels.split(' ')])
	print(sents)
	print(sents.split(' ')[0])
	predictions = pt.bigrams(sents)
	print(predictions[0])
	evaluation(predictions, labels)

"""
def main(predictions, labels):
	evaluate(predictions, labels)
"""

def main(labels):
	with open (labels, 'r') as f:
		evaluate(f.read())

if __name__ == "__main__":
	#predictions = sys.stdin.read().strip()
	labels = sys.argv[1]
	#main(predictions, labels)
	main(labels)
