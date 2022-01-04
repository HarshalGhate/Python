'''6. Write a program which accept one number and display below pattern. 
Input : 5 
Output :
 * * * * * 
 * * * * 
 * * * 
 * * 
 * '''
 
def Display(iNo):
    for i in range(0,iNo):
        for j in range(0,iNo+1):
            if(j>i):
                print("*",end=" ")
        print()    
 
def main():
    print("Enter the number :")
    iValue=int(input())
    
    Display(iValue)
 
if __name__=="__main__":
     main()