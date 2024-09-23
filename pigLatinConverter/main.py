#Jonas Fairchild Pig Latin Converter

word = input("Type the word you want to convert to Pig Latin.: ")
step1 = word[1:]
step2 = word[0]
print(step1 + step2 + "ay")