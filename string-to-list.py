# string-to-list.py

#open files
houseofusher = open("texts/houseofusher.txt", "r")
text = houseofusher.read()

# list of 'words'
wordlist = text.split()

print wordlist