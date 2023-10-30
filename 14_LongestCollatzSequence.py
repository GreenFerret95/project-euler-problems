
def get_collatz_sequence(num):
    collatz_count = 1
    new_num = 0
    while(num != 1):
        if (num % 2) == 0:  # even
            new_num = int(num/2)
            num = new_num
        else:
            new_num=(num*3) + 1
            num=new_num
        collatz_count += 1
    return collatz_count

largest_term_count = 0
largest_term = 0
current_term_count = 0
for n in range(1,1000000):
    current_term_count = get_collatz_sequence(n)
    if(current_term_count > largest_term_count):
        largest_term_count = current_term_count
        largest_term = n
    
print(f'largest_term:({largest_term}) = {largest_term_count}')
print()
