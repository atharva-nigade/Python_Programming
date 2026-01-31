# 4. Write a program which accept one number form user and return addition of its factors.
# Input : 12          Output : 16 (1, 2, 3, 4, 6)

def Facadd(value):
    sum = 0
    half = int(value/2)
    for i in range(1,half+1):
        if(value % i == 0):
            sum = sum +i
    return sum

def main():
    ret = 0
    no = 0
    no = int(input("Enter the number: "))
    ret = Facadd(no)
    print("the Addition of its factorial is :",ret)

if __name__ == "__main__":
    main()