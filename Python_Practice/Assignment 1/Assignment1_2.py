'''2. Write a program which contains one function named as ChkNum() which accept one 
parameter as number. If number is even then it should display “Even number” otherwise 
display “Odd number” on console. 
Input : 11 Output : Odd Number 
Input : 8 Output : Even Number '''

def ChkNum(iNo):
    if(iNo%2==0):
        return True;
    else:
        return False;

def main():
    print("Enter number :")
    iValue=int(input())
    
    iRet=ChkNum(iValue)
    if(iRet==True):
        print("Even Number")
    
    else:
        print("Odd number")

if __name__=="__main__":
    main()