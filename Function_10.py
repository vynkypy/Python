# Given a 2D matrix, flatten it row by row in a zigzag pattern:

def zigzag_flatten(matrix):
    result = []
    for i in range(len(matrix)):
        row = matrix[i]
        if i % 2 == 0:
            for item in row:
                result.append(item)
        else:
            for item in row[::-1]:
                result.append(item)
    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(zigzag_flatten(matrix1))
