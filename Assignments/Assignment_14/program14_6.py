# write a lambda function which accpect one number and return True if the number is odd
# otherwise False

odd = lambda No1 : No1 % 2 != 0
def main():
    ret = False
    No1 = int(input("Enter the number: "))
    ret = odd(No1)
    if(ret == True):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()