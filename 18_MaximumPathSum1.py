class Node:
    def __init__(self, number):
        self.left = None
        self.right = None
        self.number = number
        self.sum_of_self_and_ancestors = 0


def load_grid(path):
    triangle = open(path)
    grid = []
    for line in triangle:
        line.strip()
        numbers = line.split()
        grid.append(numbers)
    return grid


def build_grid_tree(grid):
    i = len(grid)-1
    parent_list_node = []
    child_nodes = []
    while i >= 1:
        if(len(child_nodes) == 0):  # initalize child_nodes with child_row
            for g in grid[i]:
                child_nodes.append(Node(g))
        else:
            parent_list_node = []
        parent_row = grid[i-1]
        for c in range(len(child_nodes)-1):
            parent = parent_row[c]
            n = Node(parent)  # parent node
            n.left = child_nodes[c]  # chlid left
            n.right = child_nodes[c+1]  # child right
            parent_list_node.append(n)
        child_nodes = parent_list_node.copy()
        i -= 1
    return parent_list_node[0]


sums = {}
largest_sum = [-1,-1]
def get_largest_sum_of_children(node, parent_sum=0):
    node.sum_of_self_and_ancestors = int(parent_sum) + int(node.number)
    if(not node.left and not node.right):
        if(node.sum_of_self_and_ancestors > largest_sum[1]):
            largest_sum[1] = node.sum_of_self_and_ancestors
            largest_sum[0] = node.number
    else:
        if node.left:
            get_largest_sum_of_children(node.left, node.sum_of_self_and_ancestors)
        if node.right:
            get_largest_sum_of_children(node.right, node.sum_of_self_and_ancestors)
    return largest_sum
    
    

#grid = load_grid("./assets/4x4_triangle.txt")
grid = load_grid("./assets/15x15_triangle.txt")

tree = build_grid_tree(grid)
largest = get_largest_sum_of_children(tree)
print(largest)