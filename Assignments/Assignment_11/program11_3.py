# write a program that accpects one number and print sum of digit  that number
# input:123
# output:6

def DigitSum(value):
    
    sum = 0
    while(value != 0):
        Digit = value % 10
        sum = sum+Digit
        value = int(value / 10) 
    return sum

def main():
    ret = 0
    No1=int(input("Enter the number:"))
    ret = DigitSum(No1)
    print("count of digit is :",ret)

    
if __name__ == "__main__":
    main()

