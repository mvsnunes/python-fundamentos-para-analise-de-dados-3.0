# basic calculator (4 operations with menu) proposed on course: Python Fundamentos Para Análise de Dados 3.0


# defining the basic operations

def add(a, b): return a+b


def sub(a, b): return a-b


def mult(a, b): return a*b


def div(a, b): return a/b


# defining variables
op = 1

# calculator
while(1):
    print("Operations:")
    print("0. Exit\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    op = input("\nOperation: ")

    if(op == '0'):
        break
    elif(op == '1'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " + ", b, " = ", add(a, b), "\n")
    elif(op == '2'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " - ", b, " = ", sub(a, b), "\n")
    elif(op == '3'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " * ", b, " = ", mult(a, b), "\n")
    elif(op == '4'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " / ", b, " = ", div(a, b), "\n")
    else:
        print("\nInvalid operation!\n")
