# 1. Write a Python program to implement a class named Demo with the following.
#   -> The class should contain two instance variables : no1 and no2.
#   -> The class should contain one class variable named Value.
#   -> Define a constructor(__init__) that accepts two parameters and initializes the instance variables.
#   -> Implement two instance methods:
#       -> Fun() - displays the values of instance variable no1 and no2.
#       -> Gun() - displays the values of instance variable no1 and no2.
#   -> Create two objects of the Demo class as follows:
#       -> Obj1 = Demo(11, 21)
#       -> Obj2 = Demo(51, 101)
#   -> Call the instance method in given sequence:
#       Obj1.Fun()
#       Obj2.Fun()
#       Obj1.Gun()
#       Obj2.Gun()
class Demo:
    value = 0
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
    def Fun(self):
        print("Inside Instance Method Fun")
        print("Instance Variable are: ",self.no1,self.no2)
    def Gun(self):
        print("Inside Instance Method Gun")        
        print("Instance Variable are : ",self.no1,self.no2)
def main():
    obj1 = Demo(11 ,21)
    obj2 = Demo(51,101)
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()
if __name__ == "__main__":
    main()
