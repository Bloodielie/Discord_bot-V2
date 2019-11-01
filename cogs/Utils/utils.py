def check_space(length):
    if length < 23:
        space = ""
        index = 23 - length
        for c in range(index):
            c = " "
            space += c
        return space
    else:
    	return " "
