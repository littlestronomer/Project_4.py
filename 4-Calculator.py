from math import sqrt

cont = True
number1 = float(input("Give the first number.\n"))
while cont:
    op = input("Give the operator.\n")
    if op == "sqrt":
        number1 = sqrt(number1)

    else:
        number2 = float(input("Give the second number.\n"))
        if op == "+":
            number1 = number1 + number2

        elif op == "-":
            number1 = number1 - number2

        elif op == "/":
            number1 = number1 / number2

        elif op == "*":
            number1 = number1 * number2

        elif op == "**":
            number1 = number1 ** number2

    print(number1)
    ask = input("Do you want to continue? [y]/n\n")
    if ask == "n":
        cont = False