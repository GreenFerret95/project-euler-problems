def increment_by_one(num_set, base):
    def recursive_increment(num_set, index):
        if index < 0:
            # If we've reached the leftmost digit and still need to increment, 
            # we need to extend the list by doubling it.
            num_set.insert(0, 0)
            index = 0

        current_value = num_set[index]
        current_value += 1

        if current_value == base:
            # If the current digit becomes equal to the base, set it to 0 and
            # increment the next digit recursively.
            num_set[index] = 0
            recursive_increment(num_set, index - 1)
        else:
            # If the current digit is less than the base, we can simply update it.
            num_set[index] = current_value

    recursive_increment(num_set, len(num_set) - 1)
    return num_set

base = 10  # Change the base as needed
n = [0]
print(n)
for i in range(20):
    n = increment_by_one(n, base)
    print(n)
