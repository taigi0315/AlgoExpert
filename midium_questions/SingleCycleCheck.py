def hasSingleCycle(array):
    start_idx = 0
    current_idx = start_idx
    visit_count = 0

    while visit_count < len(array):
        # case: pointer came back to starting index before visit all elements in the array
        if visit_count > 0 and current_idx == start_idx:
            return False
        print(current_idx)
        visit_count += 1
        current_idx = get_next_idx(array, current_idx)
        
    # case: once visit_count == len(array), return True if current_idx came back to start_idx, else return False
    return current_idx == start_idx

def get_next_idx(array, current_idx):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)
    # case: jump is negative, then calculate the next_idx by adding length of array to the next_idx
    # [-3(current), 1, 2, 3]
    # |-3, 1, 2, 3| -3(current) 1, 2, 3|-3, 1, 2, 3|
    return next_idx if next_idx >= 0 else next_idx + len(array)

