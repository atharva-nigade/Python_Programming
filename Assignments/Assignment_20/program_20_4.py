# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# • Thread ID
# • Thread Name

import threading 

def ChkUpperCase(string):
    Count = 0
    for i in string:
        if((i >= 'A') and (i <= 'Z')):
            Count = Count + 1

    print("Number of an uppercase character are: ",Count)
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)

def ChkLowercase(string):
    Count = 0
    for i in string:
        if((i >= 'a') and (i <= 'z')):
            Count = Count + 1

    print("Number of an uppercase character are:", Count)
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)

def NumericDigit(string):
    Count = 0
    for i in string:
        if((i >= '0') and (i <= '9')):
            Count = Count + 1

    print("Number of an uppercase character are:" ,Count)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)

def main():
    
    string = input("Enter the string: ")

    t1=threading.Thread(target=ChkUpperCase,args=(string,),name="capital")
    t2=threading.Thread(target=ChkLowercase,args=(string,),name="small")
    t3=threading.Thread(target=NumericDigit,args=(string,),name="Digit")
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("End of main")

if __name__ == "__main__":
    main()