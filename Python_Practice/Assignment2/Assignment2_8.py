'''8. Write a program which accept one number and display below pattern. 
Input : 5 
 
Output :
 1 
 1 2 
 1 2 3 
 1 2 3 4 
 1 2 3 4 5 '''
 
def Display(iNo):
    if(iNo<0):
        iNo=-iNo
    for i in range(1,iNo+1):
        for j in range(1,iNo+1):
            if(i==j or i>j):
                print(j,end=" ")
        print()         

def main():
    print("Enter the number :")
    iValue=int(input()) 
    Display(iValue)
 
if __name__=="__main__":
    main()