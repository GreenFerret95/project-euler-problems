def get_factorial(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f

def get_sum_of_factorial(num):
    factorial = get_factorial(num)
    s_factorial_arr = list(str(factorial))

    sum = 0
    for f in s_factorial_arr:
        sum+=int(f)
    return sum

print(get_sum_of_factorial(10))
print(get_sum_of_factorial(100))
