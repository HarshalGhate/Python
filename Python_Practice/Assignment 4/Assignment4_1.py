'''1.Write a program which contains one lambda function which accepts one parameter and return 
power of two. 
Input : 4 Output : 16 
Input : 8 Output : 64'''

Power=lambda no:no**2

def main():
    print("Enter the number :")
    iValue=int(input())
    
    iRet=Power(iValue)
    print("Power of ",iValue," is: ",iRet)    

if __name__=="__main__":
    main()