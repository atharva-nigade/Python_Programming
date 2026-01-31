# write a lambda functionusing reduce() which accepts list of numbers and return the list 
# the product of all elements

from functools import reduce

def product(values):
    ret =reduce(lambda a, b : a*b ,values)
    return (ret)

def main():
    Data = list()
    ret = 0 
    size = int(input("Enter the numer of elements: "))

    for i in range(size):
        print("Enter the",i+1,"element : ")
        Data.append(int(input()))

    print("Elements from data is : ",Data)
    ret =product(Data)
    print("the product of all elements : ",ret)

if __name__ == "__main__":
    main()
        


