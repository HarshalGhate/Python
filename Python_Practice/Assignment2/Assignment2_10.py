'''10. Write a program which accept number from user and return addition of digits in that number. 
Input : 5187934 Output : 37 '''

def SumDigits(iNo):
    iDigit=0
    iSum=0
    if(iNo<0):
        iNo=-iNo
    while(iNo!=0):
        iDigit=iNo%10
        iSum=iSum+iDigit
        iNo=iNo//10
    return iSum        

def main():
    print("Enter the number :")
    iValue=int(input())
    
    iRet=SumDigits(iValue)
    print("Addition of Digits :",iRet)

if __name__=="__main__":
    main()