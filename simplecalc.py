from math import *
def multiply(num1,num2):
    return num1*num2

def add(num1,num2):
    return num1+num2

def divide(num1,num2):
    if num2==0:
        print("Cannot divide by zero!")
    return num1/num2
def subtract(num1,num2):
    return num1-num2
def calc():
    print("A simple calculator")
    print("1.Multiply * ")
    print("2.Add + ")
    print("3.Divide / ")
    print("4.Subtract - ")

    pick=float(input("Pick the number of the operation you want to carry out (1,2,3,4): "))
    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if pick==1:
            print(multiply(num1,num2))
        elif pick==2:
            print(add(num1, num2))
        elif pick == 3:
            print(divide(num1, num2))
        elif pick == 4:
            print(subtract(num1,num2))
        else:
            print("Invalid choice.Select a number between 1 and 4")
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")


calc()