from threading import currentThread
import Utils


def increment_list(list, step):
    for i in range(len(list)):
        list[i] += step
    return list


def set_current_numbers(x_coord_check, y_coord_check, current_numbers, grid):
    for i in range(len(x_coord_check)):
        x = x_coord_check[i]
        y = y_coord_check[i]
        current_numbers[i] = int(grid[y][x])
    return current_numbers


def generate_grid_from_file(file_name):
    file = open(file_name)
    lines = file.readlines()
    grid = []
    for line in lines:
        grid.append(line.split(" "))
    return grid


def get_largest_product_by_form(x_coord_normal, y_coord_normal, storage):
    step = 1
    current_product = -1
    current_numbers = [-1, -1, -1, -1]
    x_coord_check = x_coord_normal.copy()
    y_coord_check = y_coord_normal.copy()
    should_run = True
    while(should_run):
        current_numbers = set_current_numbers(
            x_coord_check, y_coord_check, current_numbers, grid)
        current_product = Utils.get_product_of_list(current_numbers)

        # update product
        if((current_product) > products[storage]):
            products[storage] = current_product
            stored_numbers[storage] = current_numbers.copy()

        # increment next

        #------------------------------- this can be refactored into a single function
        if storage == "vertical":
            # should run?
            if (x_coord_check[3] == 19 and y_coord_check[3] == 19):
                should_run = False
            else:  # increment
                if x_coord_check[3] == grid_length_x - 1:
                    x_coord_check = x_coord_normal.copy()
                    y_coord_check = increment_list(y_coord_check, 1)
                else:
                    x_coord_check = increment_list(x_coord_check, 1)

        elif storage == "horizontal":
            if (x_coord_check[3] == 19 and y_coord_check[3] == 19):
                should_run = False
            else:  # increment
                if x_coord_check[3] == grid_length_x - 1:
                    x_coord_check = x_coord_normal.copy()
                    y_coord_check = increment_list(y_coord_check, 1)
                else:
                    x_coord_check = increment_list(x_coord_check, 1)
        elif storage == "p_diagonal":
            if (x_coord_check[3] == 19 and y_coord_check[0] == 19): # <---- only difference
                should_run = False
            else:  # increment
                if x_coord_check[3] == grid_length_x - 1:
                    x_coord_check = x_coord_normal.copy()
                    y_coord_check = increment_list(y_coord_check, 1)
                else:
                    x_coord_check = increment_list(x_coord_check, 1)

        elif storage == "n_diagonal":
            if (x_coord_check[3] == 19 and y_coord_check[3] == 19):
                should_run = False
            else:  # increment
                if x_coord_check[3] == grid_length_x - 1:
                    x_coord_check = x_coord_normal.copy()
                    y_coord_check = increment_list(y_coord_check, 1)
                else:
                    x_coord_check = increment_list(x_coord_check, 1)

    return products[storage]


grid = generate_grid_from_file("./assets/20x20Grid.txt")
grid_length_x = len(grid[0])
grid_length_y = len(grid)

products = {
    "vertical": 1,
    "horizontal": 1,
    "p_diagonal": 1,
    "n_diagonal": 1,
}
stored_numbers = {
    "vertical": [-1, -1, -1, -1],
    "horizontal": [-1, -1, -1, -1],
    "diagonal": [-1, -1, -1, -1],
}


#  vertical
x_vertical_normal = [0, 0, 0, 0]
y_vertical_normal = [0, 1, 2, 3]

# horizontal
x_horizontal_normal = [0, 1, 2, 3]
y_horizontal_normal = [0, 0, 0, 0]

# diagonal +
x_pDiagonal_normal = [0, 1, 2, 3]
y_pDiagonal_normal = [3, 2, 1, 0]

# diageonal -
x_nDiagonal_normal = [0, 1, 2, 3]
y_nDiagonal_normal = [0, 1, 2, 3]

products["vertical"] = get_largest_product_by_form(
    x_vertical_normal, y_vertical_normal, "vertical")
print(f'{stored_numbers["vertical"]} : {products["vertical"]}')

products["horizontal"] = get_largest_product_by_form(
    x_horizontal_normal, y_horizontal_normal, "horizontal")
print(f'{stored_numbers["horizontal"]} : {products["horizontal"]}')

products["p_diagonal"] = get_largest_product_by_form(
    x_pDiagonal_normal, y_pDiagonal_normal, "p_diagonal")
print(f'{stored_numbers["p_diagonal"]} : {products["p_diagonal"]}')

products["n_diagonal"] = get_largest_product_by_form(
    x_nDiagonal_normal, y_nDiagonal_normal, "n_diagonal")
print(f'{stored_numbers["n_diagonal"]} : {products["n_diagonal"]}')

print()
