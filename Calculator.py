import sys
print("\nWelcome to Calculator")

def numbers(Numbers):
    while True:
        try:
            User_input = int(input(Numbers))
            if 0 <= User_input <= sys.maxsize:
                return User_input
            elif(User_input == " "):
                print("Inputed Space bar")
            else:
                 print("Type number")
        except ValueError:
            print("Type Numbers ONLY")

def Symbol(Symbol):
    while True:
        usersymbol = input("Enter: +, -, *, %, or /: ")
        if usersymbol in ["+", "-", "*", "/"]:
            return usersymbol
        elif usersymbol == " ":
            print("You pressed Space bar")
        else:
            print("Invalid input. Please enter +, -, *, %, or /.")


FirstNumber = numbers("Type Number ")
symbol = Symbol("Type Symbol")
SecondNumber = numbers("Type SecondNumber ")

def calculate(FirstNumber,symbol,SecondNumber):
    if symbol == "+":
        return FirstNumber + SecondNumber
    elif symbol == "-":
        return FirstNumber - SecondNumber
    elif symbol == "*":
        return FirstNumber * SecondNumber
    elif symbol == "/":
        if SecondNumber !=0:
           return FirstNumber / SecondNumber
        else:
            print("Error: Division by zero.")
            return None


result = calculate(FirstNumber,symbol,SecondNumber)
print(f"You Inputed = {FirstNumber} {symbol} {SecondNumber}")
print("Your total is",result ,"\n")
