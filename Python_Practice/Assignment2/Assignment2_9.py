'''9. Write a program which accept number from user and return number of digits in that number. 
Input : 5187934 Output : 7 '''

def CountDigit(iNo):
    iCnt=0
    idigit=0
    if(iNo<0):
        iNo=-iNo
    while(iNo>0):
        idigit=iNo%10
        iCnt=iCnt+1
            
        iNo=iNo//10
    return iCnt
        

def main():
    iRet=0
    print("Enter the number :")
    iValue=int(input())
    iRet=CountDigit(iValue)
    print("Count of Digits :",iRet)

if __name__=="__main__":
    main()