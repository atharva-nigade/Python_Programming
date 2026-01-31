# write a lambda function which accepts one number and return true if it is divisible by 5

divisible = lambda No1 : No1 % 5 == 0

def main ():
    ret = False
    No1 = int(input("Enter the number : "))
    ret = divisible(No1)
    if (ret == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()