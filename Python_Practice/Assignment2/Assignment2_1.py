'''1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
parameters as number and perform the operation. Write on python program which call all the 
functions from Arithmetic module by accepting the parameters from user.'''

import Arithmetic as A

def main():
    print("Enter First number :")
    iValue1=int(input())
    print("Enter Second number :")
    iValue2=int(input())
    
    iRet=A.Add(iValue1,iValue2)
    print("Addition is :",iRet)
        
    iRet=A.Sub(iValue1,iValue2)
    print("Substraction is :",iRet)
        
    iRet=A.Mult(iValue1,iValue2)
    print("Multiplication is :",iRet)
        
    iRet=A.Div(iValue1,iValue2)
    print("Division is :",iRet)

if __name__=="__main__":
    main()
