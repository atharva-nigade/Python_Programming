# write a python program which accept N number from user and store it into list return maximun number from that list
# input:number of element:5
# input:13 5 22 44 9
# output:44

def Maximum(value):
    ret = value[0]
    for i in range(len(value)):
        if(value[i]>ret):
            ret = value[i]
    return ret

def main():
    size = 0
    Data=[]
    ret = 0

    size=int(input("Enter the number of element: "))
    Data = list()
    print("Enter the elements: ")
    
    for i in range(size):
        value = int(input())
        Data.append(value)
    Ret = Maximum(Data)
    print("Maximum number is: ",Ret)

    
if __name__ == "__main__":
    main()