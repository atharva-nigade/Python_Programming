# write a porgram which contains one function that accepts one number from user and return true if number is 
# divisible by 5 otherwise return False 
# input:8  output:False
# input:25 output:True

def Chkdiv(value):
    if(value % 5 == 0):
        return True
    else:
        return False

def main():
    ret = False
    No=int(input("enter the number: "))
    ret = Chkdiv(No)

    if(ret ==  True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()