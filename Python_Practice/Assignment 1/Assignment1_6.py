'''6.Write a program which accept number from user and check whether that number is positive or 
negative or zero. 
Input : 11 Output : Positive Number 
Input : -8 Output : Negative Number 
Input : 0 Output : Zero '''

def Check(iNo):
    if(iNo>0):
        return True
    elif(iNo<0):
        return False
    
def main():
    print("Enter the number : ")
    iValue=int(input())
    
    bRet=Check(iValue);
    
    if(bRet==True):
        print("Positive Number")
    elif(bRet==False):
        print("Negative Number")
    else:
        print("Zero")
    

if __name__=="__main__":
    main()