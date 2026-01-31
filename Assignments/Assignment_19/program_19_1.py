# Write a program which contains one lambda function which accepts one parameter and return power of two
# input:4  output:16
# intput:6 output:64

power = lambda value1: 2**value1
def main():
    No = 0
    No = int(input("Enter the number: "))
    ret = power(No)
    print("Power of the number is: ",ret)


if __name__ == "__main__":
    main()