# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # from the given descendant node,
    # track up the parent node until you meet the `topAncestor` node
    # following this logic, sample input should return
    # E: [B A], I: [D B A]

    # given two list of ancestors
    # compare from the right end to far-left till find different ancestor
    # e.g) A==A ? B == B? None == D?

    first_ancestors = find_all_ancestors(descendantOne, [])
    second_ancestors = find_all_ancestors(descendantTwo, [])
    for a in first_ancestors:
        print(a.name)
    print('---------')
    for a in second_ancestors:
        print(a.name)
    
    for idx in range(max(len(first_ancestors), len(second_ancestors))):
        # Found different ancestor, return the `last` same ancestor
        if first_ancestors[idx] != second_ancestors[idx]:
            return first_ancestors[idx-1]
        # Case one of descendant is ancestor of another descendant
        else:
            if idx == min(len(first_ancestors), len(second_ancestors))-1:
             return first_ancestors[idx]
            

def find_all_ancestors(current_node, list_of_ancestors):
    list_of_ancestors.insert(0, current_node)
    if current_node.ancestor == None:
        return list_of_ancestors
    
    return find_all_ancestors(current_node.ancestor, list_of_ancestors)

    
    
