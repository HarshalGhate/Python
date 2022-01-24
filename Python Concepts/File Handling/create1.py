def main():
    print("Enter the file name to create the file :")
    name=input()
    
    fd=0
    try:
        fd=open(name,'x')
        print("File get created with the information is :",fd)   
        
    except Exception as e:
        print("Exception Occures :",e)    
         

if __name__=="__main__":
    main();
