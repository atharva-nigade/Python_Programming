# write a program which accept one number and display below pattern
# input : 5
# output:*****
#        ****
#        ***
#        **
#       
def main():
    n = int(input("Enter the number:"))
    for i in range(n):
        
        print("*"*(n-i),)

if __name__  == "__main__":
    main()