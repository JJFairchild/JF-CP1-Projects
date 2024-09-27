word = input("Type your name and it will be turned into anagrams.: ")

import random

new1 = ''
new2 = ''
new3 = ''
new4 = ''
new5 = ''

temp1 = word
temp2 = word
temp3 = word
temp4 = word
temp5 = word

while len(temp1) != 0:
    x = random.randint(0, len(temp1) - 1)
    new1 += temp1[x]
    temp1 = temp1[0:x] + temp1[x + 1: len(temp1)]

while len(temp2) != 0:
    x = random.randint(0, len(temp2) - 1)
    new2 += temp2[x]
    temp2 = temp2[0:x] + temp2[x + 1: len(temp2)]

while len(temp3) != 0:
    x = random.randint(0, len(temp3) - 1)
    new3 += temp3[x]
    temp3 = temp3[0:x] + temp3[x + 1: len(temp3)]

while len(temp4) != 0:
    x = random.randint(0, len(temp4) - 1)
    new4 += temp4[x]
    temp4 = temp4[0:x] + temp4[x + 1: len(temp4)]

while len(temp5) != 0:
    x = random.randint(0, len(temp5) - 1)
    new5 += temp5[x]
    temp5 = temp5[0:x] + temp5[x + 1: len(temp5)]

print(f"""Your anagrams are:
{new1}
{new2}
{new3}
{new4}
{new5}
""")