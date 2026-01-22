# write a program which accpect one number and check weather it is divisible by 3 and 5
# input:15
# output:divisible by 3 and 5/

def ChkDivisible(no1):
    if (no1 % 3 == 0 and no1 % 5 == 0):
        return True
    else:
        return False


def main():
    value = False
    ret = 0
    print("enter the number:")
    no1=int(input())
    ret = ChkDivisible(no1)

    if(ret == True):
        print("divisible by 3 and 5")
    else:
        print("not divisible by 3 and 5")
    


if __name__ == "__main__":
    main()    

