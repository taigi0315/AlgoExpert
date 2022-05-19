# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	list_of_sum = []
	branch_sum_helper(root, 0, list_of_sum)
	
	return list_of_sum
	
def branch_sum_helper(root, branch_sum, list_of_sum):
	branch_sum = branch_sum + root.value
	# append branch_sum to list_of_sum when it reach down to leaf
	if not root.left and not root.right:
		list_of_sum.append(branch_sum)
		return
	# recurse the 'branch_sum_helper' down to existing branch
	if root.left:
		branch_sum_helper(root.left, branch_sum, list_of_sum)
	if root.right:
		branch_sum_helper(root.right, branch_sum, list_of_sum)
