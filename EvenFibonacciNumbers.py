'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

maxFibNumber = 4000000
fibNums = [1,2,0] # [term1, term2, termSum]
sumOfEvenFibNums = 0

while (fibNums[0] <= maxFibNumber): #currentNum under maxFibNumber
    if (fibNums[0] % 2 == 0):       #currentNum even 
        sumOfEvenFibNums+=fibNums[0]    #add to sum
        print("*" + str(fibNums[0]))
    else:
        print(fibNums[0])
        
    
    fibNums[2] = fibNums[0] + fibNums[1] #termSum = term1 + term2
    fibNums[0] = fibNums[1]         #term1 = term2
    fibNums[1] = fibNums[2]         #term2 = termSum

print(sumOfEvenFibNums)







