def find_anagrams(word, candidates):
    # A word is not its own anagram
    word = word.lower()
    
    target_dict = {}
    for letter in word:
        if letter in target_dict:
            target_dict[letter] += 1
        else:
            target_dict[letter] = 1

    
    anagrams = []
    # schleift durch Kandidaten
    for candidate in candidates:
        
        candidate_lower = candidate.lower()

        if candidate_lower == word:
            continue

        candidate_dict = {}
        # schleift durch buchstaben der kandidaten und fügt den buchstaben mit count hinzu.
        for letter in candidate_lower:
            if letter in candidate_dict:
                candidate_dict[letter] += 1
            else:
                candidate_dict[letter] = 1
                
        if candidate_dict == target_dict:
            anagrams.append(candidate)

    return anagrams
    
        
            
                
    