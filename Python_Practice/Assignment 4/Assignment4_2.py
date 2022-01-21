'''2.Write a program which contains one lambda function which accepts two parameters and return 
its multiplication. 
Input : 4 3 Output : 12 
Input : 6 3 Output : 18 '''

Multiplication=lambda iValue1,iValue2: iValue1*iValue2

def main():
    print("Enter First number :")
    iNo1=int(input())
    print("Enter Second number :")
    iNo2=int(input())
    iRet=Multiplication(iNo1,iNo2)
    print("Multiplication is :",iRet)
if __name__=="__main__":
    main()