grid = [
['A', 'B', 'C', 'A', 'D'],
['C', 'A', 'B', 'D', 'E'],
['A', 'D', 'C', 'E', 'A'],
['B', 'A', 'C', 'A', 'D'],
['D', 'C', 'B', 'E', 'A']]

Acount = 0
Bcount = 0
Ccount = 0
Dcount = 0
Ecount = 0

for collection in grid:
    for letter in collection:
        if letter == 'A':
            Acount += 1
        elif letter == 'B':
            Bcount += 1
        elif letter == 'C':
            Ccount += 1
        elif letter == 'D':
            Dcount += 1
        else:
            Ecount += 1

print(f"A: {Acount} B: {Bcount} C: {Ccount} D: {Dcount} E: {Ecount}")