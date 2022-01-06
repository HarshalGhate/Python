'''3.Write a program which accept N numbers from user and store it into List. Return Minimum 
number from that List. 
Input : Number of elements : 4 
Input Elements : 13 5 45 7 
Output : 5'''

def Minimum(Value):
    iMin=Value[0]
    for i in range(len(Value)):
        if(Value[i]<iMin):
            iMin=Value[i]
    return iMin

def main():
    iSize=0
    data=[]
    i=0
    print("Enter How many element you want ?")
    iSize=int(input())
    
    print("Enter the data")
    for i in range(iSize):
        data.append(int(input()))
    
    iRet=Minimum(data)
    print("Minimum number is :",iRet)

if __name__=="__main__":
    main()