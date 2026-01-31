# 2. Write a program which accept one number and display below pattern.
# input : 5
# Output :
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *

def display(value):
    for i in range(value):
        print("*\t"*value)

def main():
    no = 0
    no = int(input("Enter the Number: "))
    display(no)


if __name__ == "__main__":
    main()