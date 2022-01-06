no=11
print(type(no))     #<class 'int'>

no="Hello"
print(type(no))     #<class 'str'>  

no=10.5
print(type(no))     #<class 'float'> 

print("Enter the number")
value=input()

print(type(value))  #<class 'str'>     # Bydefalt all user input in python is string

no=3+5j
print(type(no))     #<class 'complex'>

data=[10,20,30,40]
print(data)
print(type(data))    #<class 'list'>

data=(10,20,30,40)
print(data)
print(type(data))     #<class 'tuple'>  

data={10,20,30,40}
print(data)
print(type(data))     #<class 'set'> 

data={"PPA":12000,"LB":12500,"Angular":11000,"Python":12500}
print(data)
print(type(data))     #<class 'dict'>
print(data.keys())     #dict_keys(['name', 'Learning'])
print(data.values())   #dict_values(['Harshal', 'Python'])