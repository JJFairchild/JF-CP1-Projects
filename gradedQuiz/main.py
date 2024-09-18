#Jonas Fairchild Graded Quiz
#Note: I know this is extremely inefficient, but I have no idea how to fix it.

points = 0

q1 = input("What is the monomer of a carbohydrate called?: ")
a1 = "monosaccharide"
if q1 == a1:
    print("Correct")
    points += 1
else:
    print("Incorrect. Correct answer: monosaccharide")

q2 = input("What is the monomer of a lipid called?: ")
a2 = "no true monomer"
if q2 == a2:
    print("Correct")
    points += 1
else:
    print("Incorrect. Correct answer: no true monomer")

q3 = input("What is the monomer of a nucleic acid called?: ")
a3 = "nucleotide"
if q3 == a3:
    print("Correct")
    points += 1
else:
    print("Incorrect. Correct answer: nucleotide")

q4 = input("What is the monomer of a protien called?: ")
a4 = "amino acid"
if q4 == a4:
    print("Correct")
    points += 1
else:
    print("Incorrect. Correct answer: amino acid")

q5 = input("What is the purpose of insulin: ")
a5 = "regulate blood sugar"
if q5 == a5:
    print("Correct")
    points += 1
else:
    print("Incorrect. Correct answer: regulate blood sugar")

print(f"Final score: {points}/5")