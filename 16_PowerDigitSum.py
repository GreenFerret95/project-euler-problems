
#EASY
 
import math

power_to =1000
p = 2
product = str(int(math.pow(p,power_to)))
result_char_arr = list(product)
sum = 0
for r in result_char_arr:
    sum+= int(r)

print(sum)