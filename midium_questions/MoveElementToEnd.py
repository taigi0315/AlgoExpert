def moveElementToEnd(array, toMove):    
    """
        initiate two indexes (idx, swap_idx)
        repeat below logic while idx > swap_idx
        
        Get number from the array (array[idx])
        Check if the number should be moved (n =? toMove)
        If yes:
            swap the number with 'last_idx'
            move last_idx to forward (last_idx -= 1)
            do not move idx since we swap, need to validate the new number
        else:
            idx += 1
    """
    
    idx = 0
    swap_idx = len(array) - 1
    
    while idx < swap_idx:
        num = array[idx]
        if num == toMove:
            swap(array, idx, swap_idx)
            swap_idx -= 1
        else:
            idx += 1

    return array

def swap(array, idx_1, idx_2):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]
