# write a lambda functionusing filter() which accepts list of number and return a 
# list of even number

def odd(values):
    ret =filter(lambda a : True if(a % 2 != 0) else False ,values)
    return list(ret)

def main():
    Data = list()
    ret = list()
    size = int(input("Enter the numer of elements: "))

    for i in range(size):
        print("Enter the",i+1,"element : ")
        Data.append(int(input()))

    print("Elements from data is : ",Data)
    ret = odd(Data)
    print("odd of elements is : ",ret)

if __name__ == "__main__":
    main()
    
