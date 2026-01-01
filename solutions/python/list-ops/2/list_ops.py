def append(list1, list2):
    return list1+list2

def concat(lists):
    result = []
    for list in lists:
        result += list
    return result

def filter(function, list):
    return [item for item in list if function(item)]

def length(list):
    return len(list)

def map(function, list):
    return [function(item) for item in list]

def foldl(function, list, initial):
    result = initial
    for i in list:
        result = function(result, i)
    return result

def foldr(function, list, initial):
    result = initial
    for i in list[::-1]:
        result = function(result, i)
    return result

def reverse(list):
    return list[::-1]
