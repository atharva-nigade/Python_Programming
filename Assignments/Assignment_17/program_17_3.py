# 3. Write a program which accept one number from user and return its factorial.
# Input : 5                   Output : 120

def factorial(value):
    product = 1
    for i in range(1,value+1):
        product=product*i
    return product

def main():
    ret = 0
    no = 0
    no = int(input("Enter the Number: "))
    ret = factorial(no)
    print("the factorial is: ",ret)

if __name__ == "__main__":
    main()