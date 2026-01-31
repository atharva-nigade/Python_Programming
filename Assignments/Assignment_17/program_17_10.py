# write a program which accept number from user and return addition of digits in that number
# input:123 
# output:6

def addition (value):
    sum = 0
    while(value != 0):
        Digit = value % 10
        sum = Digit+sum
        value = int(value/10)
    return sum

def main():
    ret = 0 
    no = 0
    no = int(input("Enter the number: "))
    ret = addition(no)
    print("Addition of digits in that number is : ",ret)

if __name__ == "__main__":
    main()