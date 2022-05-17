def isValidSubsequence(array, sequence):
    # Note sequence has to be shown in array in same order

    """
    (legnth_of_array)*(length_of_sequence) solution
    iterate through all numbers
    """

    """
    Set two pointers that points array and sequence
    if a_num == s_num -> move both pointers to next
    if a_num != s_num -> move a_pointer to next
    """
    
    # Edge case - sequence is longer than array
    if len(array) < len(sequence):
        return False

    a_idx = 0
    match_idx = []

    for s_num in sequence:
        while a_idx <= len(array) -1:
            print(f"{s_num} =? {array[a_idx]}({a_idx})")
            match = s_num == array[a_idx]
            a_idx = a_idx + 1

            if match:
                match_idx.append(a_idx)    
                break
    
        if not match:
            return False

    # Edge case: not all numbers in sequence was found
    if len(match_idx) != len(sequence):
        return False

    return True


if __name__ == "__main__":
    test_array = [5, 1, 22, 25, 6, -1, 8, 10]
    test_sequence = [1, 6, -1, 10]
    assert isValidSubsequence(test_array, test_sequence)