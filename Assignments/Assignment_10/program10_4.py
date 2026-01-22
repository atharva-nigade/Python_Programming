# write a program which accpect the number and print all even number till that number 
# input:10
# # output:2,4,6,8,10

def Even(value):
    for i in range(2,value+1,2):
        print(i)

def main():
    print("Enter the number :")
    no1=int(input())
    Even(no1)

if __name__=="__main__":
    main()