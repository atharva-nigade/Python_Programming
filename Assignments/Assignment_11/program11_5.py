def counter(value):
    count = 0
    while(value != 0):
        count = count+1
        value = int(value / 10)
    return count

def reverse(value):
    reverseddigit = 0
    digit = 0
    i = (counter(value)-1)
    while(value != 0):
        digit = value % 10
        reverseddigit = reverseddigit + (digit*(10**i))
        i = i-1
        value=int(value/10)

    return reverseddigit    

def palindrom(value):
    reversevalue = reverse(value)
    if ((reversevalue == value) == True):
        return True
    else:
        return False

def main ():
    ret = 0
    No1=int(input("enter the number:"))
    ret = palindrom(No1)
    if (ret == True):
        print("palimdrom")
    else:
        print("not palimdrom")    
    

if __name__ == "__main__":
    main()