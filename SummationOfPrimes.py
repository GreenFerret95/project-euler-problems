from timeit import default_timer
import Utils
start = default_timer()
prime_list = Utils.set_prime_list_by_value(2000000) 

print(Utils.get_sum_of_list(prime_list))
print(f'execute time: {default_timer() - start} seconds')