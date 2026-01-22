def dectobin(value):
    i = 0
    binary=0
    while (value != 0):
        remainder= value%2
        binary = binary+(remainder*(10**i))
        i = i+1
        value =int(value/2)
    return binary    



def main():
    ret = 0
    no1= int(input("enter the number:"))
    ret = dectobin(no1)
    print(ret)

if __name__ == "__main__":
    main()