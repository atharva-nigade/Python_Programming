# write a program which accepts radius of circle and prints area of circle

def circle(value):
    area = 2*3.14*value*value
    return area

def main():
    ret = 0
    no1=int(input("Enter the radius: "))
    ret = circle(no1)
    print("The area of circle is :",ret)

if __name__ == "__main__":
    main()
