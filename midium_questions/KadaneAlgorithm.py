def kadanesAlgorithm(array):
    pos_sum = [array[0]]
    for n in array[1:]:
        """
        if the last possible sum is negative and
        the last possible sum is smaller than next number
        re-start the "sum" 
        """
        if pos_sum[-1] < 0 and pos_sum[-1] < n:
            pos_sum.append(n)
        # else add next number with last possible sum
        else:
            pos_sum.append(n + pos_sum[-1])
    
    # return the maximum of all possible sum
    return max(pos_sum)

