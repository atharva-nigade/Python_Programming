#  write a program which accepts two number and print addition,substraction,multipication and diviion 

def maths (value1 , value2):
    sum = value1 + value2
    print("The Addition is:",sum)
    sub= value1 - value2
    print("The substraction is :",sub)
    mult=value1 * value2
    print("The multipication is :",mult)
    div=value1 / value2
    print("The division is :",div)
         

def main():
    
    No1 = int(input("Enter the first number:"))
    No2 = int(input("Enter the Second Number"))
    maths(No1,No2)


if __name__ == "__main__":
    main()