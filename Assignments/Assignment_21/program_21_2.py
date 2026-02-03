# Design a Python application that creates two threads.
# • Thread I should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.
import threading
def Maximum(value):
    max = value[0]
    for i in range(len(value)):
        if(value[i]>max):
            max = value[i]
    print("Maximum element from the list:  ",max)
    return max
def minimum(value):
    min = value[0]
    for i in range(len(value)):
        if(value[i]<min):
            min = value[i]
    print("minimum value form the list is: ",min)
    return min
def main():
    size = 0
    Data = []
    size=int(input("Enter the size of list: "))
    for i in range(size):
        print("Enter the element: ")
        Data.append(int(input()))
    t1 = threading.Thread(target=Maximum,args=(Data,))
    t2 = threading.Thread(target=minimum,args=(Data,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print("End of main")


if __name__ == "__main__":
    main()