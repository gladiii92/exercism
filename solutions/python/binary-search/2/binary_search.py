def find(search_list, value):
    
    left = 0
    right = len(search_list) - 1
    
    while left <= right:
        # MittelINDEX
        index = (left + right) // 2
        # MittelWERT
        mid = search_list[index]

        if mid == value:
            return index

        elif mid < value:
            left = index + 1
        else:
            right = index - 1
    
    raise ValueError("value not in array")