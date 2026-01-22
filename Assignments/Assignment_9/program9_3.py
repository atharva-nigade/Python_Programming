# write the progarm which accpect one number and print square of that number


def Square(No):
    return No * No


def main():
    ret=0
    print("enter the number: ")
    value=int(input())
    ret=Square(value)
    print("square of the number is: ",ret)




if __name__ == "__main__":
    main()