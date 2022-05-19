def nonConstructibleChange(coins):
    # populate the list with new coin by
    # adding new coin value to every elements in the list
    # edge case
    if not coins:
        return 1

    combination = []
    for c in coins:
        if not combination: 
            combination.append(c)
        else:
            copy_res = combination.copy()
            for ec in copy_res:
                combination.append(ec + c)
            combination.append(c)
    
    for i in range(1, len(combination)+1):
        if i not in combination:
            return i
    
    # edge case
    return len(combination) + 1


if __name__ == "__main__":
    assert 20 == nonConstructibleChange([5, 7, 1, 1, 2, 3, 22])
    assert 2 == nonConstructibleChange([1])