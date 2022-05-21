def productSum(array):
    sum = 0
    return productSumHelper(array, 2)

def productSumHelper(array, depth):
    sum = 0
    for n in array:
        if type(n) == list:
            sum = sum + depth * productSumHelper(n, depth+1)
        else:
            sum = sum + n
			
    return sum

if __name__ == '__main__':
    productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])