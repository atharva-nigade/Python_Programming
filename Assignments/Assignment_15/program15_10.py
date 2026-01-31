# write a lambda functionusing reduce() which accepts list of number and return the count 
# of even number
from functools import reduce
def counteven(values):
    ret =reduce(lambda count,a :count + (1 if (a % 2 == 0) else 0), values,0)
    return (ret)

def main():
    Data = list()
    ret = 0
    size = int(input("Enter the numer of elements: "))

    for i in range(size):
        print("Enter the",i+1,"element : ")
        Data.append(int(input()))

    print("Elements from data is : ",Data)
    ret =counteven(Data)
    print("numbers divisible by both 3 and 5: ",ret)

if __name__ == "__main__":
    main()
    
