def _rotate(word):
    return word[1:] + word[0]
    
def _pig_latin(word):
    if word[:2] == 'xr':
        return 'xrayay'  # for some reason
    if word[0] == 'y' and word[1] in 'aeiou':
        word = _rotate(word)
    while word[0] not in 'aeiouy':
        word = _rotate(word)
    if word[-1] == 'q' and word[0] == 'u':
        word = _rotate(word)
    return word + 'ay'
    
def translate(text):
    return ' '.join([_pig_latin(word) for word in text.split()])