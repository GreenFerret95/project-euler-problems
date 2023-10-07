import Utils
#C:\Users\bpsmi\Documents\Workspace\ProjectEuler\assets\100_50digit_numbers.txt

large_numbers = open('./assets/100_50digit_numbers.txt')
lines = large_numbers.readlines()

number_list = []

for line in lines:
    number_list.append(int(line))

sum = Utils.get_sum_of_list(number_list)
print(str(sum)[0:10])

