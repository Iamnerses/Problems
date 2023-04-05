class calc(): 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        return x+y  
    def div(self):
        return x/y
    def sub(self):
        return x-y
    def mul(self):
        return x*y
operators = ["+","-","*","/"]

class IOS_calc(calc):
    def power(self):
        return x**y

class Android_calc(calc):
    def mod(self):
        return x%y

while True:

    print(">>> WELCOME TO CALCULATOR <<<\n\nCalculator has 4 simple functions by default \n>Addition\n>Substraction\n>Multiplication\n>Division\n\n>>>")    
    calc_verse = input("Please enter calculator version to get more functions(IOS or Android):")
    if calc_verse.capitalize() == str("Ios"):
        print("You have chosed IOS\n\nHere is IOS calculator additional function\n>>>\n\n>Exponentiation(Raise to power)\n\n")
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        oper = input("Enter operator(+,-,*,/)")
        if oper == "+":        
           print( calc.sum())

    elif calc_verse.capitalize() == str("Android"):
        print("You have chosed Android\n\nHere is Android calculator function\n>>>\n\n>Modulo division\n\n")
    else:
        print("Wrong input try again")
