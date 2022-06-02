def arrayOfProducts(array):
    result = []
    for idx, num in enumerate(array):
        other_numbers = array.copy()
        other_numbers.pop(idx)
        result.append(product_array(other_numbers))

    return result

def product_array(array):
    result = 1
    for n in array:
        result = result * n
    return result
    
if __name__ == "__main__":
    assert [8, 40, 10, 20] == arrayOfProducts([5, 1, 4, 2])