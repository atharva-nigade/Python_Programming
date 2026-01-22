# write the program which accpect one number and prints factorial of that number
# input:5
# output:120

def Factorial(value):
    mult = 1
    for i in range(1,value+1):
        mult = mult*i
    return mult

def main():
    ret = 0
    print("Enter the number:")
    no1=int(input())
    ret = Factorial(no1)
    print("the factorial is : ",ret)

if __name__=="__main__":
    main()