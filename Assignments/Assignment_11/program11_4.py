# write a program that accpects one number and print reverse of digit  that number
# input:123
# output:321
def count(value):
    counter=0
    
    while(value != 0):
        Digit = value % 10
        counter = counter+1
        value = int(value / 10)
        # print(Digit)
        # print(value)
    return counter

def Reverse(value):
    reversedigits = 0
    digit = 0
    i = count(value)-1
    while(value != 0):
        digit = value % 10
        reversedigits = reversedigits + (digit*(10**i))
        i = i-1
        value = int(value/10)
    return reversedigits

def main():
    ret = 0
    No1=int(input("Enter the number:"))
    ret = Reverse(No1)
    print("reverse of digit is :",ret)

    
if __name__ == "__main__":
    main()

