import math

#checkNum = 13195
checkNum = 600851475143 #600,851,475,143 
#testUpTo = int(math.sqrt(checkNum))
#Prime = a number divisible only by 1 and itself
#Factors of checkNum

def is_prime(num):
    checkUpTo = int(math.sqrt(num))+1
    prime = True
    for i in range(2,checkUpTo):
        if(num%i==0):
            prime = False
    return prime


checkMid = int(math.sqrt(checkNum))

for x in range(1,(int(checkMid))):
    if (checkNum%x==0): #x factor of checkNum
        if(is_prime(x)):
            print("*" + str(x))
        else:
            print(x)
    


