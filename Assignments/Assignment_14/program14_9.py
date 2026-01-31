# write a lambda function which accepts two number and returns their multiplication

multipication = lambda a,b: a * b

def main():
    ret = 0
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number:"))
    ret = multipication(No1,No2)
    print("Multipication is: ",ret)

if __name__ == "__main__":
    main()