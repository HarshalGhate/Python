
def Addition(value):
    iSum=0
    for i in range(len(value)):
        iSum+=value[i]
    return iSum

def main():
    iSize=0
    data=[]
    print("How many Elements you want??")
    iSize=int(input())
    
    print("Enter the data")
    for i in range(iSize):
        data.append(int(input()))
        
    iRet=Addition(data)
    print("Addition is : ",iRet)    

if __name__=="__main__":
    main()