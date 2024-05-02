'''
1:  012 #1<2? yes switch
2:  021 #2<1? no 0<1? yes switch and shift
3:  102 #0<2? yes switch
4:  120 #2<0? no 1<0? no 1<2? yes switch and shift and reverse
5:  201 #0<1? yes switch
6:  210 #done
'''
class LexicographicPermutations:
    def __init__(self, value_list):
        self.generate(value_list)

    def flip(self,current_index, next_index, array):
        #create a copy of the array
        array_copy = array.copy()

        index_at_beginning = current_index == len(array) - 1        
        index_distance = current_index-next_index

        if(index_at_beginning):
            if(index_distance>1):
                #switch and shift
                arr_slice = array_copy[next_index:current_index]
                array[next_index] = array_copy[current_index]
                array[next_index+1::] = arr_slice
            else:
                array[next_index] = array_copy[current_index]
                array[current_index] = array_copy[next_index]
                

        else:
            #switch shift and reverse
            arr_slice = list(reversed(array[next_index+1::]))
            array[next_index] = array_copy[current_index]
            array[next_index+1::] = arr_slice
        

        return array 


        '''
        #create a copy of the array
        array_copy = array.copy()
        #put the value at current index to next index
        array_slice = []
        index_distance = (len(array)-1)-next_index
        if(index_distance==1):
            array_slice = array_copy[next_index::]
        else:
            array_slice = array_copy[next_index+1::]
        #from the original array reverse all elements from next_index to end of array
        array_slice = list(reversed(array_slice))
        array[next_index] = array[current_index]
        array[next_index::] = array_slice

        return array
        '''
        '''distance = current_index - next_index
        #swap places
        if distance == 1:
            temp = array[next_index]
            array[next_index] = array[current_index]
            array[current_index] = temp
        #put in place and move everything down by one
        else:
            array_copy = array.copy()
            current_value = array_copy[current_index]
            
            array[next_index] = array[current_index]
            for i in range(next_index+1, len(array)):
                array[i] = array_copy[i-1]
        '''



        return array
    
    def generate(self,value_list):
        index_holder = []
        for i in range(len(value_list)):
            index_holder.append(i)

        permutation_count = 1
        print(f"{value_list} -> {index_holder}")
        current_index = index_holder[len(value_list)-1]
        next_index = current_index-1

        while current_index >= 0: 
            flip_happened = False
            #if next_index is < current_index swap indexes
            if index_holder[next_index] < index_holder[current_index]:
                self.flip(current_index, next_index, value_list)
                self.flip(current_index,next_index, index_holder)
                flip_happened = True

            if flip_happened:
                print(f"{value_list} -> {index_holder}")
                permutation_count+=1
                current_index = len(value_list)-1
                next_index = current_index-1

            else:
                #move backward
                current_index =  len(value_list)-1
                if(next_index !=0):
                    next_index -=1
                else:
                    next_index = current_index-1


if __name__ == "__main__":
    value_list = ['a','b','c']
    LexicographicPermutations(value_list)