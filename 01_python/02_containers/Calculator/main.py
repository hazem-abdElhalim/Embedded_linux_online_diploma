import utils

def Calc():
    x = float(input("Enter the first number\n"))  
    y = float(input("Enter the second number\n")) 
    op = input("Enter the operation\n")
    if op == '+':
        z = utils.sum(x, y)
        print("Result:", z)
    elif op == '-':
        z = utils.sub(x, y)
        print("Result:", z)
    elif op == '*':
        z = utils.mul(x, y)
        print("Result:", z)
    elif op == '/':
        if y != 0:
            z = utils.dev(x, y)
            print("Result:", z)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    Calc()
