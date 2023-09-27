import math
import time

class Number:
    def __init__(self, number, divisors=[]):
        self.number = number
        self.divisors = divisors        
        self.sum_of_divisors = sum(divisors)
        
        if(self.sum_of_divisors < self.number):
            self.num_type = 'D'
        elif (self.sum_of_divisors > self.number):
            self.num_type = 'A'
        else:
            self.num_type = 'P'

    def __str__(self):
        return f"{self.number}: {self.divisors} - {self.sum_of_divisors} - {self.num_type}"


def generate_number_definition(num):
    divisors = set([1])
    start_num = 2
    i = start_num
    check_range = math.ceil(math.sqrt(num))
    
    for i in range(start_num, check_range + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)

    return Number(num, sorted(list(divisors)))

start_total_time = time.time()


start_num = 12
end_num = 28123
i = start_num

start_time = time.time()

abundant_numbers = set()
for i in range(start_num,end_num+1):
    num_def = generate_number_definition(i)    
    if(num_def.num_type=='A'):
        #print(num_def)
        abundant_numbers.add(num_def.number)

end_time = time.time()
elapsed_time = round(end_time - start_time,2)
print(f"Elapsed time: {elapsed_time} seconds")


#---------------------------------------------------------------------------------------------------------

sum_of_cannot_be = 0
start = 1
end = 28123

start_time = time.time()

# Create a list of numbers from start to end
numbers_to_check = list(range(start, end + 1))

for i in numbers_to_check:
    can_be_written_as_sum = False
    for abundant in abundant_numbers:
        if abundant > i // 2:
            break
        check_num = i - abundant
        if check_num in abundant_numbers:
            can_be_written_as_sum = True
            break

    if not can_be_written_as_sum:
        sum_of_cannot_be += i

end_time = time.time()
elapsed_time = round(end_time - start_time,2)
print(f"Elapsed time: {elapsed_time} seconds")

print(sum_of_cannot_be)

end_total_time = time.time()
total_elapsed = round(end_total_time - start_total_time,2)
print(f"Total Elapsed time: {total_elapsed} seconds")
