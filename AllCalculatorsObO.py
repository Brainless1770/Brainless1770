# For Addition

numberOne = int(input("Enter Number One "))

operatorOne = "Enter The Symbol from: +,-,*,/"

operatorTwo = input("Enter The Symbol: for calculation: ")

NumberTwo = int(input("Enter Number Two"))

if operatorTwo == "+":
    print(numberOne, " + ", NumberTwo, " = ", numberOne + NumberTwo)
else:
    print("Wrong")

# For Subtraction

numberOne = int(input("Enter Number One "))

operatorOne = "Enter The Symbol from: +,-,*,/"

operatorTwo = input("Enter The Symbol: for calculation: ")

NumberTwo = int(input("Enter Number Two : "))

if operatorTwo == "-":
    print(numberOne, " - ", NumberTwo, " = ", numberOne - NumberTwo)
else:
    print("Wrong")

# For  Multiplication:



numberOne = int(input("Enter Number One:  "))

operatorOne = "Enter The Symbol from: +,-,*,/"

operatorTwo = input("Enter The Symbol: for calculation: ")

NumberTwo = int(input("Enter Number Two : "))

if operatorTwo == "*":

    print(numberOne, " * ", NumberTwo, " = ", numberOne * NumberTwo)
else:

    print("Wrong")

# For Division
numberOne = int(input("Enter Number One:  "))

operatorOne = "Enter The Symbol from: +,-,*,/"

operatorTwo = input("Enter The Symbol: for calculation: ")

NumberTwo = int(input("Enter Number Two : "))

if operatorTwo == "/":

    print(numberOne, " / ", NumberTwo, " = ", int(numberOne / NumberTwo))
else:

    print("Wrong")

# For all Operators Calculator
numberOne = int(input("Enter Number One:  "))

operatorOne = "Enter The Symbol from: +,-,*,/"

operatorTwo = input("Enter The Symbol: for calculation: ")

NumberTwo = int(input("Enter Number Two : "))

if operatorTwo == "*":

    print(numberOne, " * ", NumberTwo, " = ", numberOne * NumberTwo)

elif operatorTwo == "/":

    print(numberOne, " / ", NumberTwo, " = ", numberOne / NumberTwo)

elif operatorTwo == "+":

    print(numberOne, " + ", NumberTwo, " = ", numberOne + NumberTwo)

elif operatorTwo == "-":

    print(numberOne, "-", NumberTwo, " = ", numberOne - NumberTwo)
else:
    print("Wrong data")