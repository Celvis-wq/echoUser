# echoUser.py
# Celvis

# echoUser input
def echoUserInput(inputText):
    print(inputText)

# define asking for input
def askForInput():
    userInput = input("Type something: ")
    return userInput

# define function addTwoNumbers
def addTwoNumbers(num1, num2):
    result = num1 + num2
    print("Sum:", result)

# define function multiplyThreeNumbers
def multiplyThreeNumbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

# define function determineLargestValue
def determineLargestValue(num1, num2):
    if num1 > num2:
        print("The largest number is:", num1)
    elif num1 < num2:
        print("The largest number is:", num2)
    else:
        print("Both numbers are equal.")

# ask for input then echo it back to the user
userInput = askForInput()
echoUserInput(userInput)

# ask the user to pick two numbers and print their sum
num1 = float(input("Pick a number: "))
num2 = float(input("Pick another number: "))
addTwoNumbers(num1, num2)

# ask the user to pick three numbers and print their product
num1 = float(input("Pick a number: "))
num2 = float(input("Pick another number: "))
num3 = float(input("Pick a third number: "))
product = multiplyThreeNumbers(num1, num2, num3)
print("Product:", product)

# ask the user to pick two numbers and print the largest
num1 = float(input("Pick a number: "))
num2 = float(input("Pick another number: "))
determineLargestValue(num1, num2)