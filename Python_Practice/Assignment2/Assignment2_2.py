'''2. Write a program which accept one number and display below pattern. 
Input : 5 
Output :
 * * * * * 
 * * * * *
 * * * * * 
 * * * * * 
 * * * * *'''
 
def Display(No):
    for i in range(0,No):
        for j in range(0,No):
            print("*",end=" ")
        print() 
 
def main():
    print("Enter the number :")
    iValue=int(input())
    
    Display(iValue)
 
if __name__=="__main__":
     main()