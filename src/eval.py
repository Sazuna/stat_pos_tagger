#!/bin/python3
import sys

def evaluate(predictions, labels):
	predlabels = list(zip(predictions.split(' '), labels))
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
