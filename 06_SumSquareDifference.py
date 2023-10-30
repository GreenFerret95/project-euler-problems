import math


orderedSeries = 100
sum_of_squres = 0
square_of_sum = 0

for i in range(orderedSeries+1):
    sum_of_squres+=math.pow(i, 2)

sum = 0
for i in range(orderedSeries+1):
    sum+=i
sum = math.pow(sum,2)

print(f'{sum_of_squres}')
print(f'{sum}')
print(f'{sum - sum_of_squres}')
