
def ChkPrime(iNo):
    if(iNo==1):
        return False;
    for i in range(2,int(iNo/2)+1):
        if(iNo%i==0):
            return False
    
    return True

#print(ChkPrime(17))
#print(ChkPrime(23))
#print(ChkPrime(7))
#print(ChkPrime(30))