def main():
    print("Enter the file name to enter the data :")
    name=input()
    fd=open(name,"w")
    
    print("Enter the data to write in the file :")
    data=input()
        
    fd.write(data)    
    
    fd.close()

if __name__=="__main__":
    main()