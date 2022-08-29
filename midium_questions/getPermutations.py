def getPermutations(array):
    permutations = []
    # we are going to pass the 'permutations' variable
    # and will update this when we find the new permutation combination
    helper(array, [], permutations)
    return permutations


def helper(array, perm, perms):
    # if nothing in array, append perm to perms 
    if len(array) == 0 and len(perm) > 0:
        perms.append(perm)
        # otherwise build combination
    else:
        for idx in range(len(array)):
            # simple way to remove a item in array
            next_array = array[:idx] + array[idx+1:]
            # this is how you add list (append)
            next_perm = perm + [array[idx]]
            # call the helper method with updated variables
            helper(next_array, next_perm, perms)