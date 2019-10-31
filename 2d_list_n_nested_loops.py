# 2D List & Nested Loops, Learn Python - Full Course for Beginners [Tutorial]
number_grid = [  # 2D List
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(number_grid[3][0])  # X & Y
for row in number_grid:  # Print all list into a single row
    for col in row:
        print(col)
