import os


def main():
    print("Enter the file name to delete the file :")
    name=input()
    if os.path.exists(name):
        os.remove(name)
        print("File delete sucessfully !!!")
    
    else:
        print("There is no such a file.")    
    
if __name__=="__main__":
    main();