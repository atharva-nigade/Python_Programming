# Write a program which contains one lambda function which accepts two parameter and return multpilcation
# input:4  3 output:12
# input:6 3 output:18

Multi = lambda A , B: A*B
def main():
    No1 = 0
    No2 = 0
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))
    Ret = Multi(No1,No2)
    print("Multiplication is : ",Ret)
    
if __name__ == "__main__":
    main()