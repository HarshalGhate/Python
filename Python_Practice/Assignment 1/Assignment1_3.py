'''3. Write a program which contains one function named as Add() which accepts two numbers 
from user and return addition of that two numbers. 
Input : 11 5 Output : 16 '''

def Add(ino1,ino2):
    ans=0
    ans=ino1+ino2
    return ans
    

def main():
    print("Enter first number :")
    iValue1=int(input())
    
    print("Enter Second number :")
    iValue2=int(input())
        
    iRet=Add(iValue1,iValue2)
    print("Addition is :",iRet)
    
if __name__=="__main__":
    main()