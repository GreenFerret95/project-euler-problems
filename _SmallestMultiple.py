from timeit import default_timer
import Utils
#lcm([1,10]) = 2520 
#lcm([1,20]) = 232,792,560
start = default_timer()

numbers = Utils.create_series(1,10,1)
prime_list = Utils.set_prime_list(20)

n_prime_factorizations = []
#for each number in the series get the prime factorization 
for n in range(1,len(numbers)+1):
    n_prime_factorizations.append(Utils.get_factorization(n, prime_list))


occurence_by_factor = {}
for factors in n_prime_factorizations:      # each prime_factorization in series
    if(len(factors)>0):
        for f in factors:              #
            if f not in occurence_by_factor:
                occurence_by_factor[f] = factors[f]
            else:
                if (factors[f] > occurence_by_factor[f]):
                    occurence_by_factor[f] = factors[f]

product = 1
for count in occurence_by_factor:
    for i in range(occurence_by_factor[count]):
        product*=count

print(product)
print(f'execute time: {default_timer() - start} seconds')

