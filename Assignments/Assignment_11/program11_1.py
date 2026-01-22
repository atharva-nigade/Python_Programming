# write a program which accpects one number and check whether it is prime or not
# input:11
# output:prime number

def prime(value):
    flag = True
    nohalf = int(value /2 )
    for i in range(2, nohalf+1):
        if(value % i == 0):
            flag = False
            break

    return flag


def main():
    ret = True
    print("Enter the number:")
    no1=int(input())
    ret = prime(no1)
    if (ret == True):
        print("number is prime")
    else:
        print("not prime")


if __name__ == "__main__":
    main()