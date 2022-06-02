def longestPeak(array):
    """
    1. find the peaks
    2. measure the strictly-decreasing length from the peak
    """
    if len(array) <= 2:
        return 0
    
    peaks = find_peak(array)
    peak_length = [measure_peak_length(array, p) for p in peaks]
    
    return max(peak_length) if peak_length else 0
    
def find_peak(array):
    """
    Find a index of peak from the array, return the list of peaks 
    Args:
        array (list)
    Returns:
        list of peak index 
    """
    peaks = []
    for idx in range(1, (len(array)-1)):
        num = array[idx]
        prev_num = array[idx-1]
        next_num = array[idx+1]
        if prev_num < num and num > next_num:
            peaks.append(idx)
    
    print(f"peak indexes : {peaks}")
    return peaks

def measure_peak_length(array, peak_idx):
    length = 1
    # left
    peak_num = array[peak_idx]
    print(f"peak: {peak_num}")
    left_idx = peak_idx
    right_idx = peak_idx
    
    while left_idx >= 0:
        if array[left_idx-1] < array[left_idx]:
            length += 1
            left_idx -= 1
        else:
            print(f"left stopped at {array[left_idx]}")
            break
        
    while right_idx < len(array)-1:
        if array[right_idx+1] < array[right_idx]:
            length += 1
            right_idx += 1
        else:
            print(f"right stopped at {array[right_idx]}")
            break
    print(f'length : {length}')
    return length
    
if __name__ == "__main__":
    print(longestPeak([1,2,3,3,4,0,10, 6, 5, -1, -3, 2, 3]))