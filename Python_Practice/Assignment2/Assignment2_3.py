'''3. Write a program which accept one number from user and return its factorial. 
Input : 5 Output : 120'''

def Fact(iNo):
    iMult=1
    if(iNo<0):
        return
    for i in range(1,iNo+1):
        iMult=iMult*i
    return iMult

def main():
    print("Enter the number :")
    iValue=int(input())
    
    iRet=Fact(iValue)
    print("Factorial of number :",iRet)

if __name__=="__main__":
    main()