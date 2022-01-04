'''4.Write a program which accept one number form user and return addition of its factors. 
Input : 12 Output : 16 (1+2+3+4+6)'''

def AddFact(iNo):
    iSum=0
    for i in range(1,(iNo//2)+1):
        if(iNo%i==0):
            iSum=iSum+i
    return iSum
            

def main():
    print("Enter the number :")
    iValue=int(input())
    
    iRet=AddFact(iValue)
    print("Addition of Factors :",iRet)

if __name__=="__main__":
    main()