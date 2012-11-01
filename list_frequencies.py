# list_frequency.py

import scripts1

#open files
houseofusher = open ("texts/houseofusher.txt", "r")

#turn object into string
text = houseofusher.read()

#clean up the string
text = text.lower()
text = text.replace('.','')
text = text.replace(',', '')

#turn string into an array
fullwordlist = scripts1.stripNonAlphaNum(text)

#remove particular words from the array
wordlist = scripts1.removeStopwords (fullwordlist, scripts1.stopwords)

# creates dictionary of words and associated wordcount
dictionary = scripts1.wordListToFreqDict(wordlist)

#reorders by frequency
sorteddict = scripts1.sortFreqDict(dictionary)

#print results as string
for s in sorteddict:
	print str(s)