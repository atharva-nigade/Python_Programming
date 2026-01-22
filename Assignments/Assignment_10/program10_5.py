# write a program which accpect the number and print all odd number till that number 
# input:10
# # output:1,3,5,7,9

def Odd(value):
    for i in range(1,value+1,2):
        print(i)

def main():
    print("Enter the number :")
    no1=int(input())
    Odd(no1)

if __name__=="__main__":
    main()