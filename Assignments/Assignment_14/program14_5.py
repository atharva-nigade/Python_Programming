# write a lambda function which accpect one number and return True if the number is Even 
# otherwise False
Even = lambda No1: (  No1 % 2 == 0)

def main():
    ret = False
    No1 = int(input("Enter the number: "))
    ret = Even(No1)
    if(ret == True):
        print("true")
    else:
        print("False")

if __name__ == "__main__":
    main()