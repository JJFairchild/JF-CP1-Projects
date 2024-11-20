#Jonas Fairchild, Simple Histogram

print("Input numbers until you are done, then type 'done'.")
histogramList = []
tempString = ""
tempIndex = 0

while True: #Gets an input for the user, checks for legitimacy, then adds it to the histogram list.
    tempInput = input()
    try:
        if tempInput == "done":
            break
        else:
            histogramList.append(int(tempInput))
    except:
        print("Invalid input.")

print("\n Here is your histogram: \n")
for value in histogramList: #Takes the values in the histogram list and turnes them into *s, then prints them along with an index number.
    for i in range(value):
        tempString += '*'
    tempIndex += 1
    print(f"{tempIndex}: {tempString}")
    tempString = "" 