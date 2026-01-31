# Write a program which accept N number from user and store it into list.return addition of all elements from that list
# input:Number of elements:6
# input elements:13 5 45 7 4 56
# output:130

def summation(Arr):
    sum = 0

    for i in range(len(Arr)):
        sum = sum+Arr[i]
    return sum

def main():
    size = 0
    value =0
    Ret=list()

    print("Enter the number of elements:")
    size = int(input())
    Data = list()  
    print("Enter the elemnts")

    for i in range(size):
        value = int(input())
        Data.append(value)
    
    Ret = summation(Data)
   
    print("summation is: ",Ret)    

if __name__ == "__main__":
    main()