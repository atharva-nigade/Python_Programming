# write a program which accepts number from user and return number of digit in that number,
# input :54342
# output:5

def count(value):
    counter = 0
    while(value != 0):
        digit = value % 10
        counter = counter + 1
        value = int(value/10)
        
    return counter

def main():
    ret = 0 
    no = 0
    no = int(input("Enter the number: "))
    ret = count(no)
    print("The number of digit in that number: ",ret)

if __name__ == "__main__":
    main()
