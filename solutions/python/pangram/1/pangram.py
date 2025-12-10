def is_pangram(sentence):
    # Input is ein String und Output soll Bool sein.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Edge-Cases
    if sentence == "":
        return False
    sentence = sentence.strip().lower()
    
    # Wir müssen NUR das Alphabet berücksichtigen. Wir zählen einfach alles im Dict. easy peasy.

    alphabet_counter = {}
    for ch in alphabet:
        if ch in sentence:
            print(ch)
            alphabet_counter[ch] = sentence.count(ch)
        else:
            alphabet_counter[ch] = 0
    print(alphabet_counter)
    return all(val >= 1 for val in alphabet_counter.values())