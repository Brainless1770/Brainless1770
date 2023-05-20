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