
def main():
    print("Enter the file name that you want to create :")
    name=input()
    
    fd=open(name,"x")
    
    print("File getes created with the information as :",fd)
    
if __name__=="__main__":    
    main();