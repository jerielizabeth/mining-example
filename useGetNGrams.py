#useGetNGrams.py

import scripts

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
allMyWords = wordstring.split()

print scripts.getNGrams(allMyWords, 5)