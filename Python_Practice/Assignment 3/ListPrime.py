'''5.Write a program which accept N numbers from user and store it into List. Return addition of all 
prime numbers from that List. Main python file accepts N numbers from user and pass each 
number to ChkPrime() function which is part of our user defined module named as 
MarvellousNum. Name of the function from main python file should be ListPrime(). 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 10 34 2 5 8 
Output : 54 (13 + 5 + 7 +2 + 5) '''
import MarvellousNum as M

def main():
    iSize=0
    iSum=0
    bRet=False
    data=[]
    print("How many element you want ?")
    iSize=int(input())
    
    print("Enter the elemnts")
    for i in range(iSize):
        data.append(int(input()))
        
    for i in range(len(data)):
        bRet=M.ChkPrime(data[i])
        if(bRet==True):
            iSum=iSum+data[i]
        
    print("Addition of Prime number :",iSum)
        

if __name__=="__main__":
    main()