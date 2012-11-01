# html-to-pretty-print.py
 
import scripts
 
# create dictionary of n-grams
n = 7
#open files
houseofusher = open ("texts/houseofusher.txt", "r")

#turn object into string
text = houseofusher.read()

#clean up the string
text = text.lower()
text = text.replace('.','')
text = text.replace(',', '')

fullwordlist = scripts.stripNonAlphaNum(text)
ngrams = scripts.getNGrams(fullwordlist, n)
worddict = scripts.nGramsToKWICDict(ngrams)
 
print worddict["terror"]