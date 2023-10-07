from numpy import append
import QuickSort
import Utils
'''
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
'''

def get_divisors(num):
    divisors = set()
    d1 = 1
    d2 = 2
    while(d1<d2):   #O(n/2)
        if(num%d1==0):
            d2 = int(num/d1)
            divisors.add(d1)
            if(d2!=num):
                divisors.add(d2)
        d1+=1 
    return list(divisors)


'''
perfect = 0
deficient = -1
abundant = 1
'''
def get_DPA(num):
    d = get_divisors(num)
    sum_of_divisors = Utils.get_sum_of_list(d)
    if(sum_of_divisors == num):
        return 0
    elif(sum_of_divisors < num):
        return -1
    else:
        return 1



#28124 > can be writen as sum of abundant numbers
# is 28124 / 2 an abundant number?
#print(get_DPA(28124))

abundant_numbers = []


for i in range(1, int(28124/2)):
    if(get_DPA(i) > 0): #abundant
        abundant_numbers.append(i)

a_num_set = set(abundant_numbers)
not_in_set = []
for num in abundant_numbers:
    p = num+num
    if p not in a_num_set:
        not_in_set.append(p)

print()
#QuickSort.quickSort(abundant_numbers, 0, len(abundant_numbers)-1)
print(abundant_numbers)
