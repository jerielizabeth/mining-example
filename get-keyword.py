import scripts

test = 'this test sentence has eight words in it'
ngrams = scripts.getNGrams(test.split(), 5)

print scripts.nGramsToKWICDict(ngrams)