# write the program which accpect one number and prints sum of first N natural number
# input:5
# output:15

def Natural(value):
    sum = 0
    for i in range (1,value+1):
        sum = sum +i
    return sum
        

def main():
    ret= 0
    print("enter the number: ")
    no1=int(input())
    ret = Natural(no1)
    print("sum of natural number is:",ret)

if __name__=="__main__":
    main()