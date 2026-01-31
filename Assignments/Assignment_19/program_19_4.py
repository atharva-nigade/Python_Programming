# Write a program which contains filter(), map() and reduce) in it. Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. 
# Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

def main():
    size = 0
    size = int(input("Enter the number of elements: "))

    Data=list()
    for i in range(size):
        print("Enter the Element: ")
        Data.append(int(input()))
    
    FilterList = list(filter((lambda a:True if a % 2 == 0 else False),Data))
    print("List after filter",FilterList)

    MapList = list(map(lambda a: a*a,FilterList))
    print("List after map: ",MapList)

    ReduceList = reduce(lambda a ,b :a+b,MapList )
    print("Result After Reduce: ",ReduceList)


if __name__ == "__main__":
    main()