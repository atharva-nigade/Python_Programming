# write a program which accepts one number and print that many numbers in reverse
# input:5
# output:54321

def program (value):
    
    for i in range (value,0,-1):
        print(i)

def main():
    No1=int(input("Enter the number:"))
    program(No1)

if __name__ == "__main__":
    main()