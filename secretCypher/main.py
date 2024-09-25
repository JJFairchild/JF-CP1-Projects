#Jonas Fairchild, Secret Cipher

txt = input("Type the text you want to convert to cypher. (shift = 2): ")

def map(l):
    if l == 'a':
        l = 'c'
    elif l == 'b':
        l = 'd'
    elif l == 'c':
        l = 'e'
    elif l == 'd':
        l = 'f'
    elif l == 'e':
        l = 'g'
    elif l == 'f':
        l = 'h'
    elif l == 'g':
        l = 'i'
    elif l == 'h':
        l = 'j'
    elif l == 'i':
        l = 'k'
    elif l == 'j':
        l = 'l'
    elif l == 'k':
        l = 'm'
    elif l == 'l':
        l = 'n'
    elif l == 'm':
        l = 'o'
    elif l == 'n':
        l = 'p'
    elif l == 'o':
        l = 'q'
    elif l == 'p':
        l = 'r'
    elif l == 'q':
        l = 's'
    elif l == 'r':
        l = 't'
    elif l == 's':
        l = 'u'
    elif l == 't':
        l = 'v'
    elif l == 'u':
        l = 'w'
    elif l == 'v':
        l = 'x'
    elif l == 'w':
        l = 'y'
    elif l == 'x':
        l = 'z'
    elif l == 'y':
        l = 'a'
    elif l == 'z':
        l = 'b'
    return l

newTxt = ''
num = 0
while not len(txt) == len(newTxt):
    newTxt = newTxt + map(txt[num])
    num += 1

print("Original:" + txt)
print("New:" + newTxt)