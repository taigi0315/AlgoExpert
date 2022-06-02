def isMonotonic(array):
    """
        slope = array[-1] - array[0]
        slope can be used to determine if the array should be
        monotonic-increasing or monotonic-decreasing
        if slope > 0:
            check if array is monotonic-increasing
        elif slope < 0:
            check if array is monotonic-decreasing
        else (slope == 0):
            all numbers in array should be same
    """
    if not array:
        return True
    if len(array) == 1:
        return True
    
    slope = array[-1] - array[0]
    if slope > 0:
        for idx in range(len(array)-1):
            if array[idx+1] - array[idx] < 0:
                return False
    elif slope < 0:
        for idx in range(len(array)-1):
            if array[idx+1] - array[idx] > 0:
                return False
    else:
        for idx in range(len(array)-1):
            if array[idx+1] - array[idx] != 0:
                return False
    return True
