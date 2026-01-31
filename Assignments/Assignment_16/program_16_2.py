def ChkNum(value):
    if (value%2 == 0):
        return True
    else :
        return False

def main():
    ret = False
    No = int(input("Enter the number: "))
    ret = ChkNum(No)

    if (ret == True):
        print("Even number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()