'''5.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
return Maximum number from that numbers. (You can also use normal functions instead of 
lambda functions). 
Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62] 
Output of reduce = 62'''
from functools import reduce
  
def ChkPrime(iNo):
    if(iNo==1):
        return False;
    for i in range(2,int(iNo/2)+1):
        if(iNo%i==0):
            return False
    return True

multiplication=lambda no:no*2

def ChkMax(a,b):
    if(a>b):
        return a
    else:
        return b
    
    
        
    


def main():
    iSize=0
    data=[]
    
    print("How many element You want ??")
    iSize=int(input())
    
    print("Enter the data :")
    for i in range(iSize):
        data.append(int(input()))
            
    primedata=list(filter(ChkPrime,data))
    print("List after filter =",primedata) 
    
    newdata=list(map(multiplication,primedata))           
    print("List after Map =",newdata) 
    
    maxdata=reduce(ChkMax,newdata)
    print("List after Reduce =",maxdata) 

if __name__=="__main__":
    main()