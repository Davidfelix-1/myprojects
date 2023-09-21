from tabulate import tabulate

examples_of_align = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12],
       [13, 14, 15],
]
tabular_table =tabulate(examples_of_align, headers=(['number_A_row', 'number_B_row', 'number_C_row']))
print(tabular_table)


