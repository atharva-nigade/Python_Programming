# write a lambda function which accepts three number and return largest number

from functools import reduce
def main():
    data = list()
    for i in range(3):
        print("Enter the",i+1,"element : ")
        data.append(int(input()))

    ret = reduce(lambda No1,No2 : No1 if(No1 > No2) else No2, data)
    print("largest number is: ",ret)

if __name__ == "__main__":
    main()