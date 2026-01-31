# write a lambda functionusing filter() which accepts list of string and return the list of string
#  having length greater than 5


def chkStr(values):
    ret =filter((lambda Str :True if((len(Str))>5) else False),values)
    return list(ret)

def main():
    Data = list()
    ret = list()
    size = int(input("Enter the number of elements: "))

    for i in range(size):
        print("Enter the",i+1,"string : ")
        Data.append((input()))

    print("Elements from data is : ",Data)
    ret =chkStr(Data)
    print("list of string having length greater than 5: ",ret)

if __name__ == "__main__":
    main()
    
