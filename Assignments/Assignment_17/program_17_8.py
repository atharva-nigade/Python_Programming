# write a program which accept one number and display below pattern
# input:5
# output:1
#        12
#        123
#        1234
#        12345


def main():
    no = int(input("Enter the number: "))
    for i in range(no):
        for j in range(1,i+1):
            print(j ,end=" "  )
        print()

if __name__ == "__main__":
    main()