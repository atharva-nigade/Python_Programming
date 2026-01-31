# Design a Python application that creates two threads named Threadl and Thread2.
# • Threadl should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.
# • Ensure that:
# Thread2 starts execution only after Thread 1 has completed.
# Use appropriate thread synchronizatio

import threading 

def Thread1():
    print("Numbers from 1 to 50")
    for i in range(1,50+1):
        print(i)


def Thread2():
    print("Numbers from 50 to 1 in reverse order: ")
    for i in range(50 , 0,-1):
        print(i)

def main():
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Enf of main")
if __name__ == "__main__":
    main()