# write a program which accepts number from user and print that number of "*" on screen
# input:5  
# output:*****
 
def pattern(value):
    for i in range(value):
        print(" * ",end= " ")
def main():
    
    No = int(input("Enter the number: "))
    pattern(No)
    

if __name__ == "__main__":
    main()