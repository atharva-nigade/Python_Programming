#write a program which conatin function CheckGreater() that accpects two number and prints the greater number

# input:10 20 
# output: 20 is greater

def CheckGreater(No1,No2):
    if(No1>No2):
        return No1
    else:
        return No2




def main():
    ret=0
    print("enter the frist number:")
    value1=int(input())

    print("enter the second number:")
    value2=int(input())
    ret=CheckGreater(value1,value2)
    print(ret,"is greater")

if __name__ =="__main__":
    main() 