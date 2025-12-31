def append(list1, list2):
    return list1 + list2


def concat(lists):
    # result = []
    # for package in lists:
    #     result += package
    # return result

    return [item for package in lists for item in package]

def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list] 


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in list[::-1]:
        result = function(result, item)
    return result


def reverse(list):
    # result = []
    # for i in list[::-1]:
    #     result.append(i)
    # return result
    return [i for i in list[::-1]]
