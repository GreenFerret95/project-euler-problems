from timeit import default_timer
import Utils


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


def get_triangle_number(n):
    search_up_to = int((n-1)/2)
    t_num = 0
    for i in range(0, search_up_to+1):
        first_term = i+1
        last_term = n-i
        if(first_term != last_term):
            t_num += first_term
            t_num += last_term
        else:
            t_num += first_term
    return t_num



#current best = 91.093 secs
#run2 = 116.3850597
total_start = default_timer()
'''
start_1 = default_timer()

number_count = 15000
triangle_number_by_number = {}
for i in range(number_count):
    triangle_number_by_number[i] = get_triangle_number(i)

print(f'start_1: {default_timer() - start_1} seconds')
'''
should_run = True
divisor_count = 0
current_num_check = 1

while(should_run):
    #current_triangle_num = triangle_number_by_number[current_num_check]
    current_triangle_num = get_triangle_number(current_num_check)
    divisibles = get_divisibles(current_triangle_num)
    current_divisor_count = len(divisibles)
    if(current_divisor_count > divisor_count):
        divisor_count = current_divisor_count
    if(divisor_count >= 500):        
        print(f'num:{current_num_check} t_num:{current_triangle_num} divisors:{divisor_count}')
        should_run = False
    else:
        current_num_check+=1

print(f'total_time: {default_timer() - total_start} seconds')
