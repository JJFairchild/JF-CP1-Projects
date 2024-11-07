questions = ["What is the most common acronym for Geometry Dash? (Easiest)", "Which  way do you move by default in Geometry Dash? (Easy)", "What is the most important button on the main menu? (Medium)", "Who created Geometry Dash? (Hard)", "What was the original name of Geometry Dash? (Hardest)"]
ans = ["A: GMD", "B: GDash", "C: GD", "D: GeoDash", 2, "A: Up", "B: Right", "C: Down", "D: Left", 6, "A: Workshop", "B: Play", "C: Daily Chest", "D: Character Customization", 10, "A: RobTop", "B: Nintendo", "C: Microsoft", "D: Robert Topala", 18, "A: Geometry Dash (never changed)", "B: Geometry Jump", "C: Cube Dash", "D: Shape Run", 21]
feed = ["Some people actually use this, and it's legitimately insane. Incorrect.", "While that could work, nobody calls it that. Incorrect.", "Correct!", "This is just the weirdest name ever, it's awful to say and it doesn't shorten the name at all. Incorrect.", "While this is certainly possible, it is not the default. Incorrect.", "Correct!", "If you moved down in Geometry Dash, you would die to the ground. Incorrect.", "While this is certainly possible, it is not the default. Incorrect.", "Correct!", "This button only lets you play the main levels. Incorrect.", "Nothing bad happens if you never click this button. Incorrect.", "While some players might think this is the case, it is certainly not the most important. Incorrect.", "This is not their name, it's their online username. Incorrect.", "Geometry Dash was not made by Nintendo. Incorrect.", "Geometry Dash was not made by Microsoft. Incorrect.", "Correct!", "Geometry Dash DID have an original name. Incorrect.", "Correct!", "Geometry Dash was never called 'Cube Dash'. Incorrect.", "This is literally just another way to say Geometry Dash. Incorrect."]

q = 2
score = 0
def quiz(question):
    print(questions[question])
    for i in range(5 * question, 5 * question + 4):
        print(ans[i])
    user = int(input("What answer do you choose? (use a number): ")) - 1
    print(feed[4 * question + user])
    questions[question] = "complete"
    return 5 * question + user == ans[5 * question + 4]
def check():
    i = 0
    for question in questions:
        if question == "complete":
            i += 1
    if i == 5:
        print(f"Your final score was {score}.")
    else:
        i = 0
    return i == 5

while True: 
    try:
        if quiz(q):
            score += 1
            while questions[q] == "complete":
                q += 1
        else:
            while questions[q] == "complete":
                q -= 1
    except:
        if not check():
            q = 0
            while questions[q] == "complete":
                q += 1
        else:
            break