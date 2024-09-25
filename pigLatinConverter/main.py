#Jonas Fairchild, Pig Latin Converter

word = input("Type the word you want to convert to Pig Latin.: ")

def isVowel(w, x):
    return w[x] == 'a' or w[x] == 'e' or w[x] == 'i' or w[x] == 'o' or w[x] == 'u'

w = ''
if isVowel(word, 0):
    w = 'w'

while not isVowel(word, 0):
    word = word[1:] + word[0]

print(word + w + "ay")