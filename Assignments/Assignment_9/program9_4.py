# write the progarm which accpect one number and print cube of that number

def Cube(No):
    return No * No *No


def main():
    ret=0
    print("enter the number: ")
    value=int(input())
    ret=Cube(value)
    print("cube of the number is: ",ret)




if __name__ == "__main__":
    main()