# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62


from functools import reduce

def chkprime(No):
    flag = True
    nohalf = int(No/2)

    for i in range(2,nohalf+1):
        if(No % i == 0):
            flag = False
            break
    return flag

def main():
    value = 0
    value = int(input("Enter the Number of Element: "))
    Data = list()

    for i in range(value):
        print("Enter the elements: ")
        Data.append(int(input()))

    FilterList = list(filter(chkprime,Data))
    print("List after filter is: ",FilterList)

    MapList = list(map(lambda a: a*2,FilterList))
    print("List after map: ",MapList)

    ReduceResult = reduce (lambda a,b: a if(a> b)else b,MapList)
    print("Result after Reduce: ",ReduceResult)   


if __name__ == "__main__":
    main()