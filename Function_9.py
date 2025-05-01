#   Diagonal Word Builder

def diagonal_word(grid):
    return ''.join(grid[i][i] for i in range(len(grid)))


grid1 = [
    ['P', 'a', 't'],
    ['o', 'E', 'p'],
    ['g', 's', 'N']
]
print(diagonal_word(grid1))  # Output: "PEN"
