def minimumCharactersForWords(words):
    # Write your code here.
    
    res = []
    # iterate through word in words
    for w in words:
        # copy the result list to cover the edge case that characters showed multiple times in a word
        copy_res = res.copy()
        for c in w:
            if c in copy_res:
                # remove the character from the copied result (used the character, if same character showed up, required to push to the original result)
                copy_res.remove(c)
            else:
                res.append(c)
    return res