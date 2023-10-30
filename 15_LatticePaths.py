def get_inverse(binary):

    for b in range(binary):
        if b == 0:
            binary[b] == 1
        else:
            binary[b] == 0
    return binary

def get_lattice_path_count(grid_size, i=0):
    i = 0
    while i < grid_size:
        for i in range(0,2):
            print(i)
            get_lattice_path_count(grid_size,i)
        i+=1



# grid
#for x in range(grid_length_xy[0]):
#    for y in range(grid_length_xy[1]):
#        print(f'x={x} y={y}')

# right = x++
# down = y++


#right_count < grid_x
#down_count < grid_y

# right_count+down_count = grid_x*grid_y
# move_combination = [right,right,down,down] right = 2 down = 2
#                   [right,down,right,down] right = 2 down = 2

#grid_length_xy = [2,2]
#grid_size = grid_length_xy[0] + grid_length_xy[1]
#get_lattice_path_count(grid_size,)



#create binary of length n
#increment binary
#if binary = length n / 2
#combo = true

import math
import Utils

def increment_binary(b):
    for i,e in reversed(list(enumerate(b))):
        if(e == 0):
            b[i]+=1
            break
        else:
            b[i] = 0
            b[i-1] +=1
            break
            print()

    return b
   
def get_factorial(num):
    f = 1
    for n in range(1,num+1):
        f*=n
    return f
def get_binomial_coeff(n,k):
    #n factorial
    # divided by
    #k factorial * (n-k)factorial
    nF = get_factorial(n)
    kF = get_factorial(k)    
    return (nF)/(kF * (get_factorial(n-k)))


# 2x2 = 2+2 choose 2
#20+20,2
#binomial_coeff((n+k),n)

print(int(get_binomial_coeff(40,20)))


#print(math.pow(2, 20))
print()


#2x2 = 6
#3x3 = 126
#4x4 = 
'''
xy = [20,20]
n = xy[0] * xy[1]


binary_current_arr = [str(0)]*n
binary_stop_arr = [str(1)]*n

binary_current_i = int(''.join(binary_current_arr),2)
end_join = ''.join(binary_stop_arr[0:int(len(binary_stop_arr)/2)])

binary_stop_i = int(end_join,2)

combo_list = []
while(binary_current_i <= binary_stop_i):
    #   check if sum of bin(binary_current_i) == n/2
    #binary_current_b = bin(binary_current_i)
    b_str = format(binary_current_i, 'b')
    sum_b_arr = Utils.get_sum_of_list(list(b_str))
    if(sum_b_arr <= int(binary_stop_i/2)):
        print(b_str)
        combo_list.append(b_str)
    
    binary_current_i+=1
    #   increment binary_current_i 

print(len(combo_list)*2)
'''



'''
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if(a+b+c+d) == 2:
                    print(f'[{a},{b},{c},{d}]')

print()
'''

