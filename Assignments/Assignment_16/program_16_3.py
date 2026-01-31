# write a program which contains one function named as Add() which accepts two number from user and 
# return addition of that two number
# input: 11 5
# output:16

def Add(value1,value2):
    sum= value1+value2
    return sum

def main():
    ret = 0
    No1 = int(input("Enter the first number:"))
    No2 = int(input("Enter the second number:"))
    ret = Add(No1,No2)
    print("Addition of the two number is: ",ret)


if __name__ == "__main__":
    main()