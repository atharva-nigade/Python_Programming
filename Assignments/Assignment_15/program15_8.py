# write a lambda functionusing filter() which accepts list of number and return the list of numbers
# divisible by both 3 and 5


def chkdiv(values):
    ret =filter((lambda a :True if(((a % 3) == 0) and ((a % 5) == 0)) else False),values)
    return list(ret)

def main():
    Data = list()
    ret = list()
    size = int(input("Enter the numer of elements: "))

    for i in range(size):
        print("Enter the",i+1,"element : ")
        Data.append(int(input()))

    print("Elements from data is : ",Data)
    ret =chkdiv(Data)
    print("numbers divisible by both 3 and 5: ",ret)

if __name__ == "__main__":
    main()
    
