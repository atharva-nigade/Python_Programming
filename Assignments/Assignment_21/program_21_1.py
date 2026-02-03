# Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.
import threading
def ChkPrime(value):
    flag = True
    for i in range(2,value):
        if(value % i == 0):
            flag=False
    return flag
def prime(lst):
    primelist = list(filter(ChkPrime,lst))
    print("Prime list is: ",primelist)
    return primelist 
def ChkNonPrime(value):
    flag = False
    for i in range(2,value):
        if(value% i == 0):
            flag = True 
    return flag
def Nonprime(lst):
    Nonprimelist = list(filter(ChkNonPrime,lst))
    print("NonPrime List is: ",Nonprimelist)
    return Nonprimelist
def main():
    size = 0
    Data =[]
    size = int(input("Enter the size of list: "))
    for i in range(size):
        print("Enter the element in the list: ")
        Data.append(int(input()))
    t1 = threading.Thread(target=prime,args=(Data,))
    t2 = threading.Thread(target=Nonprime,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main")
if __name__ == "__main__":
    main()