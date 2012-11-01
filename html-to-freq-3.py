# html-to-freq-3.py
 
import scripts1, scripts2

# create sorted dictionary of word-frequency pairs
#open files
houseofusher = open ("texts/houseofusher.txt", "r")

#turn object into string
text = houseofusher.read()

#clean up the string
text = text.lower()
text = text.replace('.','')
text = text.replace(',', '')

fullwordlist = scripts1.stripNonAlphaNum(text)
wordlist = scripts1.removeStopwords(fullwordlist, scripts1.stopwords)
dictionary = scripts1.wordListToFreqDict(wordlist)
sorteddict = scripts1.sortFreqDict(dictionary)

# compile dictionary into string and wrap with HTML
outstring = ""
for s in sorteddict:
    outstring += str(s)
    outstring += "<br />"
scripts2.wrapStringInHTML("html-to-freq-3", outstring)