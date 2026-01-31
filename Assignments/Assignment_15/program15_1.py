# write a lambda function  using  map () which accepts a list of numbers and returns a list 
# of squares of each number
def Squarelist(values):
    ret = map(lambda a : a**2,values)
    return list(ret)

def main():
    Data = list()
    ret = list()
    size = int(input("Enter the numer of elements: "))

    for i in range(size):
        print("Enter the",i+1,"element : ")
        Data.append(int(input()))

    print("Elements from data is : ",Data)
    ret = Squarelist(Data)
    print("Squares of elements is : ",ret)

if __name__ == "__main__":
    main()
    
