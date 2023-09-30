import math


def is_prime(num):
    checkUpTo = int(math.sqrt(num))+1
    prime = True
    for i in range(2, checkUpTo):
        if(num % i == 0):
            prime = False
            break
    return prime


def get_factorization(num, prime_list):
    factorCount = {}
    stepsSinceLastProgress = 0
    i = 0
    factorCount[1] = 1
    while(stepsSinceLastProgress <= len(prime_list)):
        currentFactor = prime_list[i]

        while(num % currentFactor == 0):  # if number can be divided by current prime evenly
            if(currentFactor not in factorCount):
                factorCount[currentFactor] = 0
            factorCount[currentFactor] += 1

            num = int(num/currentFactor)
            stepsSinceLastProgress = 0
        stepsSinceLastProgress += 1
        i += 1
        if(i >= len(prime_list)):
            i = 1
    return factorCount


def get_gcf(a, b):
    gcf = 1
    for factor in a:
        if(factor in b):
            if(factor > gcf):
                gcf = factor
    return gcf


def get_gcf_of_list(f_dict_list):
    common = set()
    product = 1
    for f_dict in f_dict_list:
        if(len(f_dict) > 0):
            for f in f_dict:
                common.add(f)
    for c in common:
        product *= c
    return product


def set_prime_list_by_length(listRange):
    primeList = []
    for i in range(2, listRange+1):
        if(is_prime(i)):
            primeList.append(i)
    return primeList


def set_prime_list_by_value(value_max):
    primeList = []
    i = 2
    while(i < value_max):
        if(is_prime(i)):
            primeList.append(i)
        i += 1

    return primeList


def create_series(start, elements, steps):
    list = []
    for i in range(start, elements+1):
        list.append(i * steps)
    return list


def get_first_n_multiples(numbers, n):
    multiple_set = set()
    n_multiple_dict = {}
    for num in numbers:
        multiple_set = set()
        for i in range(1, n+1):
            multiple_set.add(num*i)
        n_multiple_dict[num] = multiple_set
    return n_multiple_dict


def get_product_of_list(list):
    product = 1
    for l in list:
        product *= int(l)
    return product

def get_sum_of_list(list):
    sum = 0
    for l in list:
        sum += int(l)
    return sum

def increment_list(list, step):
    for i in range(len(list)):
        list[i] += step
    return list


def get_divisibles(num):
    divisors = set()
    d1 = 1
    d2 = 1
    while(d1<=d2): #    O(n)
        if(num%d1==0):
            d2 = int(num/d1)
            divisors.add(d1)
            divisors.add(d2)  
        d1+=1      
    return divisors
