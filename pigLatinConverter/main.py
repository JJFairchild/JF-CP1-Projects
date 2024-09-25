#Jonas Fairchild Pig Latin Converter

word = input("Type the word you want to convert to Pig Latin.: ")

def isVowel(w, x):
    if w[x] == 'a' or w[x] == 'e' or w[x] == 'i' or w[x] == 'o' or w[x] == 'u':
        return True
    else:
        return False

if isVowel(word, 0):
    w = 'w'
else:
    w = ''

while isVowel(word, 0) == False:
    word = word[1:] + word[0]

print(word + w + "ay")