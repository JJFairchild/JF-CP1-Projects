word = input("Type your word to see if it's a palindrome.: ")

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

revWord = reverse(word)



if word.strip() == revWord.strip():
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")