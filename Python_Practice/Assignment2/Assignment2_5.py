'''5.Write a program which accept one number for user and check whether number is prime or not. 
Input : 5 Output : It is Prime Number'''

def ChkPrime(iNo):
    if(iNo<=1):
        return False;
    for i in range(2,(iNo//2)+1):
        if(iNo%i==0):
            return False
    return True      

def main():
    bRet=False;
    print("Enter the number :")
    iValue=int(input())
    
    bRet=ChkPrime(iValue)
    if(bRet==True):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")    
    
if __name__=="__main__":
    main()