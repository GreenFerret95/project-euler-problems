from math import prod
from operator import contains
from tabnanny import check


def check_If_Palindrome(stn):
    isPalindrome = False
    stn = str(stn)
    midPoint = findMidPoint(stn)    
    bounds = [0,int(midPoint),int(midPoint),len(stn)]       # [fHStart, fHStop, sHStart, sHStop]
   
    if(midPoint%1>0):
        bounds[2] += 1
    fH = stn[bounds[0]:bounds[1]]
    sH = stn[bounds[2]:bounds[3]]
    if(fH == sH[::-1]):
        isPalindrome = True
    return isPalindrome


checkedNumbers = set()

def find_Palindromes(r):
    largest = 0
    isPalindrome = False
    product = 0
    for i in range(r+1):
        for j in range(1,i):
            product = i*j
            
            if(product not in checkedNumbers):
                if (len(str(product)) >= 2):
                    isPalindrome = check_If_Palindrome(product)
                    if(isPalindrome):
                        print(f'*{product}')
                        if(product>largest):
                            largest=product
            checkedNumbers.add(product)
    return largest



def findMidPoint(p):
    s = str(p)
    sLength = len(s)
    midPoint = sLength/2
    #print(f'{p} length {sLength} midPoint {midPoint}')
    return midPoint





print(f'largest: {find_Palindromes(999)}')


'''
r = 100
row = ""
for i in range(r):
    row += (f'\t{i}')
print(row)
for i in range(r):
    #row = f'{i}\t'
    row=""
    row += f'{str(i)}\t'
    for j in range(i):
        row += (f'{i*j}\t')
    print(row)
    '''

