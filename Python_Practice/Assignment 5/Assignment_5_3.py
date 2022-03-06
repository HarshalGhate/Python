'''3. Write a program which contains one class named as Arithmetic. 
Arithmetic class contains three instance variables as Value1 ,Value2. 
Inside init method initialise all instance variables to 0. 
There are three instance methods inside class as Accept(), Addition(), Subtraction(), 
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.'''

class Arithmetic:
    
    def __init__(self):
        self.Value1=0
        self.Value2=0
        self.Result=0
        
    def Accept(self):
        print("Enter First Number :")
        self.Value1=int(input())
        
        print("Enter second Number :")
        self.Value2=int(input())
        
    def Addition(self):
        self.Result=self.Value1+self.Value2
        return self.Result
        
    def Substraction(self):
        self.Result=self.Value1-self.Value2
        return self.Result
        
    def Multiplication(self):
        self.Result=self.Value1*self.Value2
        return self.Result
        
    def Division(self):
        self.Result=self.Value1/self.Value2
        return self.Result


def main():
    obj1=Arithmetic()    #creating obj1
    
    obj1.Accept()
    
    ret=obj1.Addition()
    print("Addition is :",ret)
    
    ret=obj1.Substraction()
    print("Substraction is :",ret)
    
    ret=obj1.Multiplication()
    print("Multiplication is :",ret)
    
    ret=obj1.Division()
    print("Division is :",ret)
    
    obj2=Arithmetic()    #creating obj2
    
    obj2.Accept()
    
    ret=obj2.Addition()
    print("Addition is :",ret)
    
    ret=obj2.Substraction()
    print("Substraction is :",ret)
    
    ret=obj2.Multiplication()
    print("Multiplication is :",ret)
    
    ret=obj2.Division()
    print("Division is :",ret)  
if __name__=="__main__":
    main()