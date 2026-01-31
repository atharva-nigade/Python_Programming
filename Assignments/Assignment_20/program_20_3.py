# Design a Python application that creates two threads named Even List and OddList.
# • Both threads should accept a list of integers as input.
# • The Even List thread should:
# • Extract all even elements from the list.
# • Calculate and display their sum.
# • The OddList thread should:
# • Extract all odd elements from the list.
# • Calculate and display their sum.
# • Threads should run concurrently.

import threading

def EvenList(value):
    sum = 0
    for i in range(len(value)):
        if(value[i] % 2 == 0):
            sum =sum+value[i]

    print("Addition of Even Element in list : ", sum)
    return sum
            
def OddList(value):
    sum = 0
    for i in range(len(value)):
        if(value[i] % 2 != 0):
            sum =sum+value[i]

    print("Addition of Odd Element in list : ", sum)
    return sum

def main():
    no = 0
    Data=[]
    no = int(input("Enter the size of list: "))

    for i in range(no):
        print(f"Enter the {i+1} number :")
        Data.append(int(input()))

    t1 = threading.Thread(target=EvenList,args=(Data,))
    t2 = threading.Thread(target=OddList,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

