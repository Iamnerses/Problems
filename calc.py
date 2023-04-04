class calc: 
    def sum(x,y):
        return x+y  
    def div(x,y):
        return x/y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y

class IOS_calc(calc):
    def power(x,y):
        return x**y

class Android_calc(calc):
    def mod(x,y):
        return x%y



print(">>>\n\nCalculator has 4 simple functions by default \n>Addition\n>Substraction\n>Multiplication\n>Division\n\n>>>")    
calc_verse = input("Please enter calculator version to get more functions(IOS or Android):")
if calc_verse.capitalize() == str("Ios"):
    print("You have chosed IOS\n\nHere are IOS calculator additional function\n>>>\n\n>Exponentiation(Raise to power)\n\n")
 

elif calc_verse.capitalize() == str("Android"):
    print("You have chosed Android\n\nHere are Android calculator functions\n>>>\n\n>Modulo")
    while True:
        
       cont=str(input("Enter Yes to quit"))
       break:
else:
    print("Wrong input try again")
