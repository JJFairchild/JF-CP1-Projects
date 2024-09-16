word = input("Type your word to see if it's a palindrome. (extremely strict): ")

def isPalindrome(str):
    return str == str[::-1]

if isPalindrome(word):
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")