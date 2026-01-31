# write a lambda function which accpets the two numbers and return maximum number

maximum = lambda value1 , value2: value1 if (value1 >value2) else value2
def main():
    
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))
    ret = (maximum(No1,No2))
    print("maximun number is: ",ret)

if __name__ == "__main__":
    main()    