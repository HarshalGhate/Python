# Named function
def Add(a,b):
    return a+b

# Lambda function
AddX = lambda a,b : a+b

def main():
    ret = Add(10,20)
    print("Addition is : ",ret)

    ret = AddX(10,20)
    print("Addition is : ",ret)

    print(type(Add))
    print(type(AddX))
    print(lambda a,b : a+b)

if __name__ == "__main__":
    main()


# def Function_Name(Parameters):
#    Function_Body

# lambda parameters : expression