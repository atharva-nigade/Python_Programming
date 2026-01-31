# Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def Even():
    EvenCount = 0
    i = 1
    while(EvenCount < 10):
        if(i % 2 == 0):
            print(i)
            EvenCount = EvenCount + 1

        i = i+1

def odd():
    OddCount = 0
    i = 1
    while(OddCount < 10):
        if(i % 2 != 0):
            print(i)
            OddCount = OddCount + 1

        i = i+1

def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=odd)

    t1.start()
    t1.join()

    t2.start() 
    t2.join()

    print("End of main")
if __name__ == "__main__":
    main()