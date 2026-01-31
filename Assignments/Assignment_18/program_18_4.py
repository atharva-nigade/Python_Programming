# write a python program which accept N number from user and store it into list return frequency of that number from that list
# input:number of element:5
# input:13 5 45 7 4 56 5 34 2 5 65
# elememt to search:5
# output:3
def Frequency(value):
    count=0
    serach = int(input("Element to search: "))
    for i in range(len(value)):
        if (serach ==value[i]):
            count = count +1
    return count

def main():
    size = 0
    Data = 0
    ret = 0

    size=int(input("Enter the number of elements: "))
    Data = list()
    print("Enter the elements: ")

    for i in range(size):
        value = int(input())
        Data.append(value)
    ret = Frequency(Data)
    print("Frequency of element is : ",ret)
if __name__ == "__main__":
    main()