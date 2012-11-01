# html-to-kwic.py

import scripts1, scripts2, scripts3

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

fullwordlist = scripts1.stripNonAlphaNum(text)
ngrams = scripts3.getNGrams(fullwordlist, n)
worddict = scripts3.nGramsToKWICDict(ngrams)

# output KWIC and wrap with html
target = 'terror'
outstr = ""
if worddict.has_key(target):
    for k in worddict[target]:
        outstr += str(k)
        outstr += '<br />'
else:
    outstr += 'Keyword not found in source'
scripts2.wrapStringInHTML('html-to-kwic', outstr)
