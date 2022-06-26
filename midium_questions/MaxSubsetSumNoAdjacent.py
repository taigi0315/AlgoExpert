def maxSubsetSumNoAdjacent(array):
    # return 0 if array is empty
    if array == []:
        return 0
    # return bigger number when array has two numbers
    if len(array) <= 2:
        return max(array)
    # return max of two possible case
    if len(array) == 3:
        return max([(array[0]+array[2]), array[1]])
    # calculate two cuases
    pick_first = array[0] + maxSubsetSumNoAdjacent(array[2:])
    pick_second = array[1] + maxSubsetSumNoAdjacent(array[3:])

    return max([pick_first, pick_second])