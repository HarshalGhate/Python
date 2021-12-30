'''9. Write a program which display first 10 even numbers on screen. 
Output : 2 4 6 8 10 12 14 16 18 20 '''

def Display(iNo):
    for i in range(1,iNo+1):
        print(i*2,end=" ")

def main():
    print("Enter the number :")
    iValue=int(input())
    Display(iValue)

if __name__=="__main__":
    main()