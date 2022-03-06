'''1.Write a program which contains one class named as Demo. 
Demo class contains two instance variables as no1 ,no2. 
That class contains one class variable as Value. 
There are two instance methods of class as Fun and Gun which displays values of instance 
variables. 
Initialise instance variable in init method by accepting the values from user.
 
After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()'''


class Demo:
    Value=12
    def __init__(self,a,b):
        self.no1=a
        self.no2=b        
        
    def fun(self):
        print(self.no1)
        print(self.no2)
    
    def gun(self):
        print(self.no1)
        print(self.no2)        


def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)
    
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()
    

if __name__=="__main__":
    main()