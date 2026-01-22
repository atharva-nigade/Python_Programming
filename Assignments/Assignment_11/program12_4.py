# write a program which accepts one number and print that many numbers statring from 1
# input:5
# output:12345

def program (value):
    for i in range(1, value+1):
        print(i)
        
def main():
    No1 = int(input("enter the number : "))
    program(No1)
    
if __name__ == "__main__":
    main()