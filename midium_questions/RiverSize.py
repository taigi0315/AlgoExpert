def riverSizes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    res = []
    visited = [[False for c in range(cols)] for r in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if visited[r][c] == False and matrix[r][c] == 1:
                river_size = find_water(matrix, visited, r, c)
                res.append(river_size)

    return res

def find_water(matrix, visited, row, col):
    if row not in range(len(matrix)) or col not in range(len(matrix[0])):
        return 0
    
    if matrix[row][col] == 0 or visited[row][col] == 1:
        return 0
    
    river_size = 0
    visited[row][col] = True

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in direction:
        river_size += find_water(matrix, visited, row+dx, col+dy)

    return 1 + river_size

            