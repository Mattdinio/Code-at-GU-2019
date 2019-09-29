 # Question 1
 def divisibleByThree ():
    for i in range(1,101):
        if i % 3 == 0:
            print (i)
# Question 2
def shakespeare ():
    quote = ""

# Question 3
def numberThing():
    for i in range (1,11):
        if i % 3 == 0:
            print (i**3)
        elif i % 2 == 0:
            print (i**2)
        else:
            print (i)

# Please feel free this main which has a simple interface for testing
def main():
    questionNumber = input("what question do you want to run? ")
    while questionNumber.isdigit() == False:
        questionNumber = input("what question do you want to run? ")
    questionNumber = int(questionNumber)
    if questionNumber == 1:
        divisibleByThree()
    elif questionNumber == 2:
        print ("question Incomplete")
    elif questionNumber == 3:
        numberThing()
    else:
        print("question not found")
    yesResponses = ["Yes","yes","YEs","YES","yEs","yES"]
    noResponses = ["no","No","NO","nO"]
    userContinue = input("do you want to pick another question to run? (yes / no)")
    while userContinue not in yesResponses and userContinue not in noResponses:
        userContinue = input("do you want to pick another question to run? (yes / no)")
    if userContinue in yesResponses:
        main()
    else:
        quit()