def levenshteinDistance(str1, str2):
    # Create empty 2d table to calculate the minimum edit
    table = [[0 for s1 in range(len(str1)+1)] for s2 in range(len(str2)+1)]
    # Fill up the first column
    for c in range(len(str1)+1):
        table[0][c] = c
    # Fill up the first row
    for r in range(len(str2)+1):
        table[r][0] = r

    # Fill up the table following the rule
    # if letters in column and row are same, fill the spot with the number from upper/left
    # else fill up the spot with min(upper-left, upper, left) + 1
    for c in range(1, len(str1)+1):
        for r in range(1, len(str2)+1):
            if str1[c-1] == str2[r-1]:
                table[r][c] = table[r-1][c-1]
            else:
                table[r][c] = min(table[r-1][c-1], table[r-1][c], table[r][c-1]) + 1
    
    print(table)
    return table[-1][-1]