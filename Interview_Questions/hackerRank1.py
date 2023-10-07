#Amazon Demo question 1
#split one set of boxes into 2
# a is minimal
# a > b
# a union b = arr
# a interset b = null

def minimalHeaviestSetA(arr):
    heaviestSet = []
    heaviest_sum = 0
    current_heaviest_sum = 0
    total_sum = 0
    for a in arr:
        total_sum += a
    for i in range(len(arr)):        
        for j in range(len(arr)):
            if(i!=j):
                current_heaviest_sum = arr[i]+arr[j]
                remainder = total_sum - current_heaviest_sum
                if(current_heaviest_sum > remainder):
                    if(current_heaviest_sum > heaviest_sum):
                        heaviest_sum = current_heaviest_sum
                        heaviestSet.append([arr[i],arr[j]])

    greatest_set = []
    greatest = 0
    for h in heaviestSet:
        sum = h[0] + h[1]
        if(sum > greatest):
            greatest_set = h
            greatest = sum
    greatest_set.sort()
    return greatest_set
    



arr1 = [5,3,2,4,1,2]
arr2 = [3,7,5,6,2]
print(minimalHeaviestSetA(arr2))
