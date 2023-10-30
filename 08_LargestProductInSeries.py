
from unicodedata import digit

def get_product_of_list(list):
    product = 1
    for l in list:
        product*=l
    return product

d = []

digit_file = open('./assets/digits.txt')
lines = digit_file.readlines()

digits = {'0','1','2','3','4','5','6','7','8','9'}
for line in lines:
    for i in line:
        if(i in digits):
            d.append(int(i))

search_size = 13
search_element_start = 0
search_element_stop = search_element_start+search_size

largets_product = 1
while(search_element_stop <= len(d)):
    d_range = d[search_element_start:search_element_stop]
    p = get_product_of_list(d_range)
    if(p>largets_product):
        largets_product = p
    search_element_start+=1
    search_element_stop+=1

print()