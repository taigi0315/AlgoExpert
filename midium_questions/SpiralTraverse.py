def spiralTraverse(array):
    # Cover edge case
    if not array:
        return []
    
    res = []
    direction = 'right'
     
    while True:
        # Get shape of the 2d array
        n, m = len(array[0]), len(array)
        
        if n == 1: # vertical elements last
            if direction in ['right', 'down']:
                for l in array:
                    res.extend(l)
            else:
                temp = []
                for l in array:
                    temp.extend(l)
                res.extend(temp[::-1])
            return res
        
        if m == 1: # horizon element
            if direction in ['right', 'up']:
                for l in array:
                    res.extend(array[0])
            else:
                res.extend(array[0][::-1])
            return res
        # if n >=2 and m >= 2        
        if n >= 2 and m >= 2:
            if direction == 'right':
                array, res = read_right(array, res)
                direction = 'down'
            elif direction == 'down':
                array, res = read_down(array, res)
                direction = 'left'
            elif direction == 'left':
                array, res = read_left(array, res)
                direction = 'up'
            elif direction == 'up':
                array, res = read_up(array, res)
                direction = 'right'
            else:
                raise Exception(f"Unexpected Direction : {direction}")
        show_process(array, direction)
    return res
     
def show_process(array, direction):
    print(array)
    print(direction)

def read_right(array, res):
    res.extend(array[0])
    # cut off top side of the 2d array
    return array[1:], res

def read_down(array, res):
    temp = []
    for l in array:
        temp.append(l[-1])
    res.extend(temp)
    # cut off right side of the 2d array
    return [l[:-1] for l in array], res

def read_left(array, res):
    # reverse order of last list
    res.extend(array[-1][::-1])
    # cut off bottom side of the 2d array
    return array[:-1], res

def read_up(array, res):
    temp = []
    for l in array:
        temp.append(l[0])
    # reverse order or first elements from each list
    res.extend(temp[::-1])
    # cut off left side of the 2d array
    return [l[1:] for l in array], res