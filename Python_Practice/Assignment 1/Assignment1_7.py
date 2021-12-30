'''7. Write a program which contains one function that accept one number from user and returns 
true if number is divisible by 5 otherwise return false. 
Input : 8 Output : False 
Input : 25 Output : True '''

def ChkDivisibleFive(iNo):
    if(iNo%5==0):
        return True
    else:
        return False

def main():
    print("Enter the number")
    iValue=int(input())
    
    iRet=ChkDivisibleFive(iValue)
    if(iRet==True):
        print("Number is divisible by 5")
    else:
        print("Number is not Divisible by 5")        

if __name__=="__main__":
    main()