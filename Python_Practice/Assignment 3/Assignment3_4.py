'''4.Write a program which accept N numbers from user and store it into List. Accept one another 
number from user and return frequency of that number from List. 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
Element to search : 5 
Output : 3 '''

def CountFreq(Arr,iNo):
    iCnt=0
    for i in range(len(Arr)):
        if(Arr[i]==iNo):
            iCnt+=1
    return iCnt


def main():
    iSize=0
    data=[]
    print("How many elements you want ?")
    iSize=int(input())
    
    print("Enter the data")
    for i in range(iSize):
        data.append(int(input()))
    
    print("Enter the number to count frequency :")
    iValue=int(input())
    
    iRet=CountFreq(data,iValue)
    print("Frequency of ",iValue,"is :",iRet)

if __name__=="__main__":
    main()