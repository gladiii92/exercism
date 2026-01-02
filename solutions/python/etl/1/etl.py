def transform(legacy_data):
    new_data = {}
    
    for key, val in legacy_data.items():
        for letter in val:
            new_data[letter.lower()] = key
    return new_data