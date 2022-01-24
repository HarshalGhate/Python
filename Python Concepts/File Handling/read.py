import os

def main():
    print("Enter the file name to open the file : ")
    name=input()
    
    if os.path.exists(name):    
        fd=open(name,"r")
        
        data=fd.read()  
        
        fd.close()  
        
        print("Data of the file :",data)        
    else:
        print("There is no file")
    
if __name__=="__main__":
    main()