# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List - [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce
def main():
    size = 0
    size = int(input("Enter the size of list: "))
    
    Data = list()
    print("Enter the elements: ")
    for i in range(size):
        value=int(input())
        Data.append(value)
    
    Filterlist = list(filter((lambda no :True if (no>= 70 and no<=90) else False),Data))
    print("List After Filter: ",Filterlist)

    Maplist=list(map(lambda No: No+10,Filterlist))
    print("List After Map: ",Maplist)

    Reduceresult=reduce(lambda No1,No2:No1*No2,Maplist)
    print("Product of all number: ",Reduceresult)

if __name__ == "__main__":
    main()