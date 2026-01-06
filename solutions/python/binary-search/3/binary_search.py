def find(search_list, value):
    # index
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        current = search_list[mid]
        if current == value:
            return mid
        elif current < value:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError("value not in array")