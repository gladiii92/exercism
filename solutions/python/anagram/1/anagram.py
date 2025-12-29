def find_anagrams(word, candidates):
    word = word.lower()
    target_dict = {}

    for letter in word:
        if letter in target_dict:
            target_dict[letter] += 1
        else:
            target_dict[letter] = 1
    result = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        candidate_dict = {}

        if candidate_lower == word:
            continue
        for letter in candidate_lower:
            if letter in candidate_dict:
                candidate_dict[letter] += 1
            else:
                candidate_dict[letter] = 1
        if target_dict == candidate_dict:
            result.append(candidate)
    return result
