from numpy import sort
import Utils
# d(n)
# sum of proper divisors of n
# numbers less than n which divide eveninly into n


def d(n):
    div = list(Utils.get_divisibles(n))
    div = sort(div)
    sum = Utils.get_sum_of_list(div[0:len(div)-1])
    return sum


def print_Dn(n, Dn):
    print(f'd({n})={Dn}')


# if d(a) = b
    # and d(b) = a
    # and a != b
    # a and b are amicable pair

'''
n = [220,284]

Dn = [d(n[0]),d(n[1])]
print_Dn(n[0],Dn[0])
print_Dn(n[1],Dn[1])
'''

n_range = 10000
n_Dn = {}

amicable_nums = set()
for a in range(2, n_range):
    dA = d(a)  # b
    dB = d(dA)  # a
    if ((a == dB) and (a != dA)):
        amicable_nums.add(a)
        amicable_nums.add(dA)

sum = 0
for a in list(amicable_nums):
    sum += a

print(sum)
