'''4.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204'''

from functools import reduce

ChkEven=lambda no:(no%2==0)

Square=lambda no:no**2

Addition=lambda no1,no2:no1+no2

def main():
    iSize=0
    data=[]
    
    print("How many Elements you want ?")
    iSize=int(input())
    
    print("Enter the data :")
    for i in range(iSize):
        data.append(int(input()))
        
    newdata=list(filter(ChkEven,data))
    print("List after Filter",newdata)
    
    Squaredata=list(map(Square,newdata))
    print("List After Map",Squaredata)
    
    iRet=reduce(Addition,Squaredata)
    print("Addition of Reduce",iRet)
if __name__=="__main__":
    main()