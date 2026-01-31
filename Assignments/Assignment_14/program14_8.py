# write a lambda function which accepts two number and return ther addition

Addition = lambda a , b : a+b

def main():
    ret = 0
    No1 = int(input("Enter the  first number: "))
    No2 = int(input("Enter the second number: "))
    ret = Addition(No1,No2)
    print("Addition is :",ret)

if __name__ == "__main__":
    main()