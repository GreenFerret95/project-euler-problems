limit = 1000

sum = 0
for i in range(1, limit + 1):
    sum += i ** i

how_many_digits = 10
str_sum = str(sum)[-how_many_digits:] # - for last 10 digits
print(str_sum)

