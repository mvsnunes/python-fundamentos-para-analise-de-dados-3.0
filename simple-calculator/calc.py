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
    if(op == '1'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " + ", b, " = ", add(a, b), "\n")
    if(op == '2'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " - ", b, " = ", sub(a, b), "\n")
    if(op == '3'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " * ", b, " = ", mult(a, b), "\n")
    if(op == '4'):
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("\n", a, " / ", b, " = ", div(a, b), "\n")
    if(op != '1' and op != '2' and op != '3' and op != '4' and op != '0'):
        print("\nInvalid operation!\n")
