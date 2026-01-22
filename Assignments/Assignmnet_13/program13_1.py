# write a program which accepts length and width of rectange and prints area
def rectange(value1,value2):
    area =value1*value2
    return area


def main():
    ret = 0
    No1=int(input("Enter the length:"))
    No2=int(input("Enter the width:"))
    ret = rectange(No1,No2 )  
    print("The area is:",ret)

if __name__ == "__main__":
    main()    
