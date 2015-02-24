"""
@author Mike Bartoli
Classifies gender of names using naive baye

"""

from nltk.corpus import names
import nltk
import random

def gender_features(word):
	return {'last_letter': word[-1]}

names = ([(name, 'male') for name in names.words('male.txt')] + 
	 [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print classifier.classify(gender_features(raw_input("Enter a name\n")))

