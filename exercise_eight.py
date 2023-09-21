from tabulate import tabulate

table_of_square_and_cube = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 4, 8],
    [3, 9,27],
    [4,16,64],
    [5,25,125],
]


tabular_table = tabulate(table_of_square_and_cube, headers=['number', 'square', 'cube'])
print(tabular_table)