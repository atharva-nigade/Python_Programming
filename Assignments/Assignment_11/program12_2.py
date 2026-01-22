# write a program ehich accpets one number and print its factor
# input:12
# output:1 2 3 4 6 12

def program(value):
    for i in range(1,value+1):
        if (value % i == 0):
            print(i)


def main():
    print("Enter the number: ")
    No1=int(input())
    program(No1)

if __name__ == "__main__":
    main()
