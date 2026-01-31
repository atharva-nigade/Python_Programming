# Design a Python application that creates two threads named Even Factor and OddFactor.
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors.
# The OddFactor thread should:
# Identify all odd factors of the given numffer.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message:
# "Exit from main"

import threading

def evenFactor(value):
    sum = 0
    for i in range(1,value+1):
        if(value % i == 0 and i%2 == 0):
            print("even factor: ",i)
            sum = sum +i
    print("Addition of EvenFactor is: ",sum)  

def OddFactor(value):
    sum = 0
    
    for i in range(1,value+1):
        if(value % i == 0 and i % 2 != 0):
            print("odd factor: ",i)
            sum = sum +i
    print("Addition of OddFactor is: ",sum) 

def main():
    no = 0
    no = int(input("Enter the number: "))

    t1=threading.Thread(target=evenFactor , args=(no,))
    t2=threading.Thread(target=OddFactor , args=(no,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
