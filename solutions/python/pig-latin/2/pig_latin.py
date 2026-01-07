"""
1. Input. 
- Es kommt ein String in die Funktion mit dem Parameter "text". 
- Ja. 
- Leerzeichen ja -> .split(" ") nutzen?

2. Output 
- einen bearbeiteten String 
- Ja Reihenfolge der Wörter bleibt gleich. 
- Jedes Wort wird anhand verschiedener Regeln bearbeitet.

3. Denkprozess - was muss ich wie aufbauen?
- Wie teilen wir die Aufgabe richtig auf?
    1. Sonderfälle/Ausnahmen?
    2. allgemein Regeln?
    3. welche Regel vor allen anderen? 
    4. erster Vokal suchen!
    5. was ist mit qu?
    6. was mit y?

4. Welche Regeln wie abarbeiten?
- Regel 1 - sofort aussortierbar
- Regel 4 - y 
- Regel 3 
- Regel 2

# Hilfsfunktionen nötig? Ja!
# 1. zum transformieren des einzelnen Texts
# 2. zum bestimmen des Indexes/Vokals

5. 
1. translate(text) -> wörter splitten und richtig vorbereiten -> tarnslate_word(word)
2. translate_word(word)
-> Regel 1 .startswith((xr, yt), vokal) return word + ay
-> Regel 4 startswith(y) -> transform(word, 1) -> findet ersten Vokal -> find_first_vowel(word), falls kein Vokal -> Sonderfall
-> Regel 3 qu -> transform(word, index+1)
-> Standardfall -> transform(word, index)

3. transform(word, index) -> Wort ab index + Wort bis index + "ay"
4. find_first_vowel(word) -> schleife über letter und index mit enumerate für letter und index -> Index zurückgeben
5. translate(text) -> map translate_word auf alle Wöter -> Ergebniss wieder zu String zusammensetzen mit join.
"""
VOWELS = "aeiou"
VOWELS_PLUS = VOWELS + "y"

def find_first_vowel(word):
    for idx, ch in enumerate(word):
        if ch in VOWELS_PLUS:
            return idx
    return -1

def transform_word(word, index):
    return word[index:] + word[:index] + "ay"

def translate_word(word):
    # Regel 1
    if word.startswith(("xr", "yt", VOWELS_PLUS)):
        return word + "ay"
    # Regel 4
    if word.startswith("y"):
        return transform_word(word, 1)
    # Standardfall - Regel 2
    index = find_first_vowel(word)
    if index == -1:
        return word
    # Regel 3: qu davor
    if word[index-1:index+1] == "qu":
        return transform_word(word, index + 1)
        
    # Standard-Konsonanten-Fall
    return transform_word(word, index)

def translate(text):
    words = text.split(" ")
    translated_words = map(translate_word, words)
    return " ".join(translated_words)
