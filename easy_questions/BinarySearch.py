def binarySearch(array, target):
    	# edge case
	if not array:
		return False
	if len(array) == 1:
		return 0 if array[0] == target else -1
	print(array)
	print(target)
    # init left, right pointer
	left = 0
	right = len(array)-1
	# iterate till find the target or 
	# confirm target does not exist in array
	
	while True:
		mid = int((left + right)/2)
		print(left, right, mid)
		if mid == 0:
			# could not find the target
			return 0 if array[0] == target else -1
		if right-left == 1:
			# edge case that last two numbers left
			if array[left] == target:
				return left 
			if array[right] == target:
				return right
			return -1
		
		if array[mid] == target:
			# found target
			return mid
		elif array[mid] > target:
			# target is on left
			right = mid
		elif array[mid] < target:
			# target is on right
			left = mid

		
		