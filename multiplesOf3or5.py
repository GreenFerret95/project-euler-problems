multiples = [3,5]
sum = 0
rangeMax = 1000

for i in range(rangeMax):
    if ((i % multiples[0] == 0) or (i % multiples[1] == 0)):
        sum += i

print(sum)

