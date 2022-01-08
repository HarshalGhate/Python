from functools import reduce
print("Data after reduce : ",reduce(lambda a,b : a+b,(list(map(lambda no : no + 2,(list(filter(lambda no : (no % 2 == 0),[5,7,6,8,4])))))
)))
