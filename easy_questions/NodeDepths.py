def nodeDepths(root):
    # Write your code here.
	# Set initial depth
    depth = []
    start_depth = 0
    node_depth_helper(root, start_depth, depth)
	
    return sum(depth)

def node_depth_helper(root, current_depth, depth):
	# update total depth
	
	depth.append(current_depth)
	print(f'depth : {depth}, current_depth : {current_depth}')
	if root.left:
		node_depth_helper(root.left, current_depth + 1, depth)
	if root.right:
		node_depth_helper(root.right, current_depth + 1, depth)
	if not root.left and not root.right:
		return
		
	
	

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
