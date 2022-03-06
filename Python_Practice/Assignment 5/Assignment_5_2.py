'''2. Write a program which contains one class named as Circle. 
Circle class contains three instance variables as Radius ,Area, Circumference. 
That class contains one class variable as PI which is initialise to 3.14. 
Inside init method initialise all instance variables to 0.0. 
There are three instance methods in side class as Accept(), CalculateArea() , 
CalculateCircumference(), Display().
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance 
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area, 
Circumference.
After designing the above class call all instance methods by creating multiple objects.'''

class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumferance=0.0
            
    def Accept(self):
        print("Enter the Radius :")
        self.Radius=int(input())        
    
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius**2
            
    def CalcualateCircumferance(self):
        self.Circumferance=2*Circle.PI*self.Radius
           
    def Display(self):
        print("Value of Radius : ",self.Radius)
        print("Area of Circle : ",self.Area)
        print("Circumfarance of Circle : ",self.Circumferance)

def main():
    obj1=Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalcualateCircumferance() 
    obj1.Display()   

    obj2=Circle()
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalcualateCircumferance() 
    obj2.Display()
if __name__=="__main__":
    main()