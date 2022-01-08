from functools import reduce
def main():
    data = [5,7,6,8,4]

    print("Original data : ", data)
    newdata = list(filter(lambda no : (no % 2 == 0),data))

    print("Data after filter : ",newdata)
    incrementdata = list(map(lambda no : no + 2,newdata))

    print("Data after map : ",incrementdata)
    ret = reduce(lambda a,b : a+b,incrementdata)

    print("Data after reduce : ",ret)

if __name__ == "__main__":
    main()