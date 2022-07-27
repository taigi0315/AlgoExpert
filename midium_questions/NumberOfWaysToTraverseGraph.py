def numberOfWaysToTraverseGraph(width, height):
    if width == 0:
        return 1
    if height == 0:
        return 1
    
    # Create a table to calculate the path
    table = [[0 for w in range(width)] for h in range(height)]
    # Fill up the first row and column path
    for w in range(width):
        table[0][w] = 1
    for h in range(height):
        table[h][0] = 1

    # fill up the path
    for w in range(1, width):
        for h in range(1, height):

            table[h][w] = table[h-1][w] + table[h][w-1]
    
    for row in table:
        print(row)
    
    return table[-1][-1]
            