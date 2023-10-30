from enum import Enum

class Number(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10

    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEN = 14
    FIFTEEN = 15
    SIXTEEN = 16
    SEVENTEEN = 17
    EIGHTEEN = 18
    NINETEEN = 19

    TWENTY = 20
    THIRTY = 30
    FORTY = 40
    FIFTY = 50
    SIXTY = 60
    SEVENTY = 70
    EIGHTY = 80
    NINETY = 90

def get_english_from_number(num):
    n_char_arr = []
    n_list = list(str(num))
    for nL in n_list:
        n_char_arr.append(Number(int(nL)).name)
    r_n_char_arr = list(reversed(n_char_arr))
    i = len(r_n_char_arr)-1
    is_hundred = False
    while i > 0:
        if(i == (4-1)):
            r_n_char_arr[i] = f'{r_n_char_arr[i]} THOUSAND'
        elif(i == (3-1)):   #HUNDRED
            is_hundred = True
            r_n_char_arr[i] = f'{r_n_char_arr[i]} HUNDRED'
        elif(i >= 1):   #TENS
            tens_place = (Number[r_n_char_arr[i]].value)*10  # """
            ones = Number[r_n_char_arr[i-1]].value
            current_number = int(tens_place)+int(ones)

            if current_number <= 19:
                r_n_char_arr[i] = f'{Number(current_number).name}'
                r_n_char_arr.pop(i-1)
                break
            else:
                r_n_char_arr[i] = f'{Number(tens_place).name}'
                r_n_char_arr[i-1] = f'{Number(ones).name}'
                break
        i -= 1

    result = []
    for i in range(len(r_n_char_arr)):
        if(is_hundred):
            #AND GOES WHERE
            if num%100 != 0:
                if('HUNDRED' in r_n_char_arr[i]):
                    r_n_char_arr[i] = f'{r_n_char_arr[i]} AND'
     
        if 'ZERO' not in r_n_char_arr[i]:
            result.append(r_n_char_arr[i])
            
    result.reverse()
    result_str = ' '.join(result)     
    sum_str = result_str.replace(' ', '')
    print(sum_str)

    return len(sum_str)

sum_of_letters = 0
for i in range(1,1000+1):
    sum_of_letters += get_english_from_number(i)
print(sum_of_letters)