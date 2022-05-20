def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	redShirtHeights = sorted(redShirtHeights)
	blueShirtHeights = sorted(blueShirtHeights)
	print(redShirtHeights)
	print(blueShirtHeights)
	if redShirtHeights[0] == blueShirtHeights[0]:
		return False
	# red goes second row
	if redShirtHeights[0] > blueShirtHeights[0]:
		for i in range(len(redShirtHeights)):
			if redShirtHeights[i] <= blueShirtHeights[i]:
				return False
	# blue goes second row
    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False    

    return True
