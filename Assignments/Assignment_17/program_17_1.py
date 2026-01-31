# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub[]
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation, Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.
import Arithmetic

def main():
    No1=int(input("Enter the first number: "))
    No2=int(input("Enter the second Number: "))

    print("addition is: ",Arithmetic.Add(No1,No2))
    print("substraction is: ",Arithmetic.Sub(No1,No2))
    print("Division is: ",Arithmetic.div(No1,No2))
    print("Multiplication is: ",Arithmetic.Mult(No1,No2))

if __name__ == "__main__":
    main()
