from math import *

def quadraticEquation(A,B,C):
    #List of Variables
    a = float(A)
    b = float(B)
    c = float(C)
    d = 0.0
    e = 0.0
    equation = ""
    f = 0.0
    #Checking if input can be a quadratic equation. Will return if not.
    if a == 0:
        print("The inputed values cannot make a quadratic equation.")
        return
    #Displaying the equation
    equation = str(a) + "x^2"
    if b > 0:
        equation = equation + " + " + str(b) + "x"
    elif b < 0:
        equation = equation + " - " + str(-b) + "x"
    if c > 0:
        equation = equation + " + " + str(c)
    elif c < 0:
        equation = equation + " - " + str(-c)
    #Calculating the discriminant: (b^2 - 4ac)
    d = (b*b) - (4.0 * a * c)
    #Evaluating the discriminant
    #If d > 0, there are solutions when x = ((-b +/- sqrt(d))/2a)
    if(d > 0.0):
        d = sqrt(d)
        e = (-b + d)/(2.0*a)
        f = (-b - d)/(2.0*a)
        print("There are two solutions to the equation " + equation + ".")
        print("There is a solution when x = " + str(e) + " and when x = " + str(f) + ".")
    #If d = 0, there is only one solution: when x = -b/2a
    elif(d == 0.0):
        e = (-b)/(2.0*a)
        print("There is one solution to the equation " + equation + ".")
        print("There is a solution when x = " + str(e) + ".")
    #If d < 0, there is nonreal solutions: when x = -b/2a +/- i(sqrt(d)/2a)
    else:
        d = sqrt(-d)
        e = (-b/2.0*a)
        f = (d/2.0*a)
        print("There is no real solutions to the equation " + equation + ".")
        print("The nonreal solutions are when x = " + str(e) + " +/- " + str(f) + "i.") 

#Applying the function
def main():
    firstInput = input("Enter a number")
    secondInput = input("Enter a number")
    thirdInput = input("Enter a number")
    quadraticEquation(firstInput,secondInput,thirdInput)
    
main()
