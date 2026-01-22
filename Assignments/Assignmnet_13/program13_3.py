

def prefect(value):
    sum =0
    half=int(value/2)
    for i in range(1,half+1):
        if(value % i == 0 ):
            sum = sum+i
    if(value == sum ):
        return True
    else:
        return False   

def main(): 
    ret = 0
    no1= int(input("enter the number:"))
    ret = prefect(no1)
    if(ret == True):
        print("it is a perfect number")
    else:
        print("it is not a perfect number")    

if __name__ == "__main__":
    main()


