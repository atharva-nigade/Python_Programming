# write a lambda function which accpets the two numbers and return minimum number
minimum = lambda value1 , value2:value1 if value1<value2 else value2
def main():
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number"))
    ret = minimum(No1,No2)
    print("the minimum number is: ",ret)
if __name__ == "__main__":
    main()