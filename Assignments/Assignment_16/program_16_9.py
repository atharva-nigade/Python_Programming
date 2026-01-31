# write a program which accept name from user and display length of its Name
# input:marvellous 
# output:10

def display(value):
    print(len(value))
    

def main():
    #ret = 0
    name = input("Enter the name: ")
    display(name)
    #print("Length of its name is: ",ret)


if __name__ == "__main__":
    main()