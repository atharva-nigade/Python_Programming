# Design a Python application where multiple threads update a shared variable.
# • Use a Lock to avoid race conditions.
# • Each thread should increment the shared counter multiple times.
# • Display the final value of the counter after all threads complete execution.

import threading


a = 0

lobj = threading.Lock()

def Increment():
    global a
    with lobj:
        for i in range(10):
            a = a + 1
            print(a)

def Decrement():
    global a

    with lobj:
        for i in range(5):
            a = a - 1
            print(a)


def main():
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Decrement)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

    print("Main : ", a)

if __name__ == "__main__":
    main()
