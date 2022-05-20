def tandemBicycle(redShirtSpeeds:list , blueShirtSpeeds:list, fastest:bool)->int:
    """
    tandembicycle's speed is decided by faster speed
    
    Args:
        redShirtSpeeds (_type_): _description_
        blueShirtSpeeds (_type_): _description_
        fastest (_type_): _description_

    Returns:
        _type_: _description_
    """
    print(redShirtSpeeds)
    print(blueShirtSpeeds)
    print(fastest)

    if fastest:
        # since faster speed decide the speed of bicycle,
        # We can find fastest combination by 
        # sort out total speed and choose top n 
        return sum(sorted(redShirtSpeeds + blueShirtSpeeds)[-len(redShirtSpeeds):])
    
    else: #minimum
        # We can find minimum speed by pairng red and blue that is same rank in each team, 
        red = sorted(redShirtSpeeds)
        blue = sorted(blueShirtSpeeds)
        return sum([max(r,b) for r, b in zip(red, blue)])
    
