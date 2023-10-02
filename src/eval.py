#!/bin/python3
import sys

"""
fref, fhyp = sys.argv[1], sys.argv[2]
tokscmp = []
sentscmp = []
with open(fref) as refsents, open(fhyp) as hypsents:
	for refsent, hypsent in zip(refsents, hypsents):
		print(refsent, hypsent)
		for reftok, hyptok in zip(refsent, hypsent):
			tokscmp.append(reftok == hyptok)
		sentscmp.append(refsent == hypsent)
print(sum(tokscmp), len(tokscmp), sum(tokscmp)/len(tokscmp))
print(sum(sentscmp), len(sentscmp), sum(sentscmp)/len(sentscmp))
"""
def evaluate(predictions, labels):
	print(predictions)
	print(labels)
	predlabels = list(zip(predictions.split(' '), labels))
	print(predlabels)
	errors = 0
	correct = 0
	for predlabel in predlabels:
		pred, label = predlabel[0].split('/'), predlabel[1].split('/')
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
			
			

def main(predictions, labels):
	evaluate(predictions, labels)

if __name__ == "__main__":
	predictions = sys.stdin.read().strip()
	labels = sys.argv[1:]
	main(predictions, labels)
