grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[0])         # [1, 2, 3]  → the whole first row
print(grid[1][2])       # 6          → row 1, then position 2 within that row → value 6
print(grid[2][0])       # 7          → row 2, position 0


# Looping through a 2D list — print every value
for row in grid:
    for value in row:
        print(value, end=" ")
print()