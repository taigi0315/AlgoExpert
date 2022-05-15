


def twoNumberSum(array: list , targetSum: int):
    # Could be done by brute force search (lengh_of_numbers)^2 times

    """
    1. for numbers in list of numbers
    2. Check if pair number(target-selected_number) is in list_of_numbers_checked ---> (length_of_numbers) times at most
    3. if yes, we found two numbers
    4. if not
        append number to list_of_numbers_checked
        go to next number
    """
    checkd_numbers = []
    for n in array:
        pair_number = targetSum - n
        if pair_number in checkd_numbers:
            print(f"Found pairs, reurning {[n, pair_number]}")
            return [n, pair_number]
        else:
            checkd_numbers.append(n)
    print(f'There was no pair of numbers in given list that sum is equal to {targetSum}')
    return []




if __name__ == '__main__':
    # Test
    assert twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]