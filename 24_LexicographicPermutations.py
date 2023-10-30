class PTree:
    root_number = None
    TreeList = []
    def __init__(self,root_number: int, child_numbers, len_of_child_numbers,list_so_far:list[int]) -> None:
        self.root_number = root_number
        while(len_of_child_numbers> 0):
            if len_of_child_numbers ==1:
                new_root = child_numbers[0]
                list_so_far.append(new_root)
                self.TreeList.append(PTree(new_root,[],0,list(list_so_far)))
            else:
                for i in range(0, len_of_child_numbers-1):
                    new_root = child_numbers[i]
                    the_rest = child_numbers[:i] + child_numbers[i + 1:]
                    list_so_far.append(new_root)
                    self.TreeList.append(PTree(new_root,the_rest,len(the_rest),list(list_so_far)))
        if len_of_child_numbers ==0:

            print(''.join(list(map(str,list_so_far))))

class PermuationWorker:
    def __init__(self, permutation_numbers) -> None:
        tree = self.GeneratePermutationTree(permutation_numbers)

    def GeneratePermutationTree(self, permuation_numbers) -> PTree:
        #for i in range(0, len(permuation_numbers)-1):
        root = permuation_numbers[0]
        rest = permuation_numbers[1:]
        list_so_far = [root]
        copy = list(list_so_far)
        p = PTree(root,rest,len(rest),copy)
        print()




permutation_numbers = [1, 2, 3]

p = PermuationWorker(permutation_numbers)
print()


