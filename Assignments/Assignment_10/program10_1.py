# write a program which accpect one number and print multiplication table of that number
# input:4
# output:4 8 12 16 20

def MultiTable(value):
    for i in range(1,11):
        print(value*i)
        



def main():

    print("Enter the Number : ")
    no1=int(input())
    MultiTable(no1)




if __name__ == "__main__":
    main()