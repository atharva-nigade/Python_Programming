# 3 Write a Python program to implement a class named Arithmetic with the following characteristics:

#   -> The class should contain two instance variables: Valuel and Value2.
#   -> Define a constructor (init) that initializes all instance variables to 0.
#   -> Implement the following instance methods:
#       -> Accept() - accepts values for Valuel and Value2 from the user.
#       -> Addition() - returns the addition of Valuel and Value2.
#       -> Subtraction() - returns the subtraction of Valuel and Value2.
#       -> Multiplication() - returns the multiplication of Valuel and Value2.
#       -> Division() - returns the division of Valuel and Value2 (handle division by zero properly).
#   ->Create multiple objects of the Arithmetic class and invoke all the instance methods

class Arithmetic:
    def __init__(self):
        self.value1=0.0
        self.value2=0.0

    def Accept(self):
        print("Enter the First Number: ")
        A = float(input())
        self.value1=A
        print("Enter the second number:")
        B = float(input())
        self.value2=B

    def Addition(self):
        add = 0.0
        add = self.value1+self.value2
        return add
    
    def Substraction(self):
        sub = 0.0
        sub = self.value1-self.value2
        return sub
    
    def Multiplication(self):
        mult=0.0
        mult=self.value1*self.value2
        return mult
    
    def Division(self):
        Div=0.0
        Div = (self.value1 / self.value2)
        return Div
    
    def Display(self):
        print("Addition is: ",self.Addition())
        print("substraction is: ",self.Substraction())
        print("multiplication is: ",self.Multiplication())
        print("Division is: ",self.Division())

def main():

    obj1=Arithmetic()
    obj2=Arithmetic()
    obj3=Arithmetic()
    obj4=Arithmetic()
    obj5=Arithmetic()

    obj1.Accept()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()
    obj1.Display()

    obj1.Accept()
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()
    obj2.Display()

    obj1.Accept()
    obj3.Addition()
    obj3.Substraction()
    obj3.Multiplication()
    obj3.Division()
    obj3.Display()

    obj1.Accept()
    obj4.Addition()
    obj4.Substraction()
    obj4.Multiplication()
    obj4.Division()
    obj4.Display()

    obj1.Accept()
    obj5.Addition()
    obj5.Substraction()
    obj5.Multiplication()
    obj5.Division()
    obj5.Display()

    print("End of main")

if __name__ == "__main__":
    main()


    
    

