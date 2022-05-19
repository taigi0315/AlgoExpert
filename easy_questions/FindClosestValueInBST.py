def findClosestValueInBst(tree, target):
	return findClosestValueHelper(tree, target, float('inf'))

def findClosestValueHelper(tree, target, closest_value):
	if tree.value == target:
		return tree.value
	# update closest value if need
	if abs(tree.value - target) < abs(closest_value - target):
		closest_value = tree.value
	# right branch exist, and value is closer
	if tree.right and tree.value < target:
		return findClosestValueHelper(tree.right, target, closest_value)
	if tree.left and tree.value > target:
		return findClosestValueHelper(tree.left, target, closest_value)
	return closest_value
		


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None









if __name__ == '__main__':
    # Test
    assert findClosestValueInBst()