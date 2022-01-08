'''4.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204'''

from functools import reduce

Even=lambda no: no%2==0

Increment=lambda no : no**2

Sum=lambda a,b: a+b


def main():
    iSize=0
    data=[]
    
    print("How many Elements you Want??")
    iSize=int(input())  
    
    print("Enter the data :")
    for i in range(iSize):
        data.append(int(input()))
    
    evendata=list(filter(Even,data))  
    print("After Filter data :",evendata)
    
    Incrementdata=list(map(Increment,evendata))
    print("After Map data :",Incrementdata)
    
    Sumdata=reduce(Sum,Incrementdata)
    print("After Reduce data :",Sumdata)

if __name__=="__main__":
    main()