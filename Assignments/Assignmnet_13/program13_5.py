def marks(value):

    if(value >= 75):
        print("distinction")
    elif( value >= 60):
        print("first class") 
    elif( value >= 50):
        print("second class") 
    elif( value <50):
        print("fail") 

def main():
    no1=int(input("enter the marks:"))
    marks(no1)


if __name__ == "__main__":
    main()