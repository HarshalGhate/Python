'''10. Write a program which accept name from user and display length of its name. 
Input : Marvellous Output : 10'''

def Length(str):
    result=len(str)
    return result
    

def main():
    print("Enter the string ")
    cValue=input()
    iRet=Length(cValue)
    print("String length :",iRet)
if __name__=="__main__":
    main()