def smallestDifference(arrayOne, arrayTwo):
    # Sort two given arrays
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    
    # initiate the index on each array
    idx_1, idx_2 = 0, 0
    # initiate min_distance
    min_distance = float('inf')
    min_pair = []
    
    
    # calcualte the distance
    
    # if distance is smaller than min_distance, update
    while True:
        num_1 = arrayOne[idx_1]
        num_2 = arrayTwo[idx_2]
        distance = abs(num_1 - num_2)    
        if distance < min_distance:
            min_distance = distance
            min_pair = [num_1, num_2]
        
        # if num_one > num_two ==> move index_2 vice versa
        if num_1 <= num_2:
            idx_1 += 1
        else:
            idx_2 += 1
        # while index_1, index_2 < length of each array    
        if idx_1 == len(arrayOne) or idx_2 == len(arrayTwo):
            break
    
    return min_pair