import QuickSort
# Extra Challenge= Try implenting sort without libary
# Failed lol

#nums = [9,5,3,2,7,3,1,4]
#QuickSort.quickSort(nums, 0, len(nums)-1)


def create_alpha_unicode_map():
    a_uni_map = {}
    for i in range(65, 65+26):
        a_uni_map[chr(i)] = i-64
    return a_uni_map

def get_name_sum(str):
    name_sum = 0
    for c in list(str):
        name_sum += uni_map[c]
    return name_sum

def get_name_score(name_score, index):
    return name_score*index
names = open("./Assets/p022_names.txt").readlines()[0].split(",")
for i in range(len(names)):
    names[i] = names[i].replace("\"", "")


QuickSort.quickSort(names, 0, len(names)-1)
uni_map = create_alpha_unicode_map()


#print(get_name_score(get_name_sum('COLIN'), 938))

total_name_score = 0
for i in range(0, len(names)):
    name_index = i+1
    name_sum = get_name_sum(names[i])
    name_score = get_name_score(name_sum, name_index) 
    total_name_score += name_score

print(total_name_score)


