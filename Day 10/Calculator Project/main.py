from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

calculations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculate(n1,n2,operand):
    return calculations[operand](n1,n2)


n1=float(input("Please enter the first number : "))
restart_new=True
while restart_new:
    operand=input("Please enter the type of operation '+' or '-' or '*' or '/' :")
    n2=float(input("Please enter the second number: "))
    res=calculate(n1,n2,operand)
    print(f"{n1}{operand}{n2}={res}")
    restart=input(f"Do you want to start a new calculation with the previous result {res} enter 'y' for yes and 'n' for no: ")
    if restart=="y":
        n1=res
    else:
        restart_new=False