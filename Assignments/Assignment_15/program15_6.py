# write a lambda functionusing reduce() which accepts list of number and return the minimum elements

from functools import reduce

def minimum(values):
    ret =reduce(lambda a, b : a if a<b else b ,values)
    return (ret)

def main():
    Data = list()
    ret = 0 
    size = int(input("Enter the numer of elements: "))

    for i in range(size):
        print("Enter the",i+1,"element : ")
        Data.append(int(input()))

    print("Elements from data is : ",Data)
    ret =minimum(Data)
    print("Minimum of elements is : ",ret)

if __name__ == "__main__":
    main()
    
