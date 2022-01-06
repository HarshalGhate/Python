'''2.Write a program which accept N numbers from user and store it into List. Return Maximum 
number from that List. 
Input : Number of elements : 7 
Input Elements : 13 5 45 7 4 56 34 
Output : 56 '''

def Maximum(Value):
    iMax=0
    for i in range(len(Value)):
        if(Value[i]>iMax):
            iMax=Value[i]
    return iMax        


def main():
    iSize=0
    data=[]
    i=0
    print("Enter How many element you want ?")
    iSize=int(input())
    
    print("Enter the data")
    for i in range(iSize):
        data.append(int(input()))
    
    iRet=Maximum(data)
    print("Maximum number is :",iRet)

if __name__=="__main__":
    main()