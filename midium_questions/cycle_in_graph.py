def cycleInGraph(edges):
    # Write your code here.
    # we can use depth-first-search
    for idx in range(len(edges)):
        # iterate through each starting idx
        if find_cycle(idx, edges):
            return True

    # No cycle fond from any starting index
    return False

def find_cycle(start_idx, edges):
    # deepth-first serach starting from given idx
    # return True if find cycle or return False
    #idx:
    #edges

    stack = [start_idx]
    visit = set()

    while len(stack) > 0:
        current_node = stack.pop()
        next_nodes = edges[current_node]
        # if any edges are connected to start_idx
        # cycle was found, return True
        if start_idx in next_nodes:
            return True
        else:
            # Add current node to visited node list
            visit.add(current_node)
            for c_n in next_nodes:
                if c_n not in visit:
                    stack.append(c_n)

    return False
    
    