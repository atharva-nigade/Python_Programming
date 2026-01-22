# write a program that accpects one number and print count of digit i that number
# input:7521
# output:4

def count(value):
    counter=0
    
    while(value != 0):
        Digit = value % 10
        counter = counter+1
        value = int(value / 10)
        # print(Digit)
        # print(value)
    return counter

    

def main():
    ret = 0
    No1=int(input("Enter the number:"))
    ret = count(No1)
    print("count of digit is :",ret)

    
if __name__ == "__main__":
    main()


