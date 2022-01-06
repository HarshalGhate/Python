'''1.Write a program which accept N numbers from user and store it into List. Return addition of all 
elements from that List. 
Input : Number of elements : 6 
Input Elements : 13 5 45 7 4 56 
Output : 130 '''

def Addition(value):
    isum=0
    for i in range(len(value)):
        isum=isum+value[i]
    return isum    

def main():
    i=0
    iSize=0
    data=[]
    print("Enter How many element you want ??")
    iSize=int(input())
    
    print("Enter the Elements :")
    for i in range(iSize):
        data.append(int(input()))
    
    iRet=Addition(data)
    print("Addition of List :",iRet)

if __name__=="__main__":
    main()
