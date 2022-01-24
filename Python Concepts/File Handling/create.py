

from venv import create


def main():
    print("Enter the file name to create :")    
    name=input()
    
    fd=open(name,"x")
    print("File get created with the information :",fd)
    
if __name__=="__main__":
    main();