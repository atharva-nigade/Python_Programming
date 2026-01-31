# Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading

def addition(value):
    sum = 0
    for i in range(len(value)):
        sum = sum +value[i]
    print("sum of elements in list: ",sum) 

def multiplication(value):
    product = 1
    for i in range(len(value)):
        product = product*value[i]
    print("product of  element in the list:",product)

def main():
    size = 0
    Data = []
    size = int(input("Enter the size: "))
    for i in range(size):
        print("Enter the element: ")
        Data.append(int(input()))
    
    t1 = threading.Thread(target=addition,args=(Data,))
    t2 = threading.Thread(target=multiplication,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("En of main")


if __name__ == "__main__":
    main()