'''4.Write a program which display 5 times Marvellous on screen. 
Output : Marvellous 
 Marvellous 
 Marvellous 
 Marvellous 
 Marvellous '''
 
def Display(iNo):
    for i in range(0,5):
         print("Marvellous")
 
def main():
     print("Enter the number")
     iValue=int(input())
     Display(iValue)
      
if __name__=="__main__":
     main()