def flatten(iterable):

    result = []

    for package in iterable:
        if isinstance(package, (tuple, list)):
            result += flatten(package)
        elif package is not None:
            result.append(package)
    return result