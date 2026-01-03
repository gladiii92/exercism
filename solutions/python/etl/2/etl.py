def transform(legacy_data):
    new_dict = {}
    for key, val in legacy_data.items():
        for letter in val:
            new_dict[letter.lower()] = key
    return new_dict
