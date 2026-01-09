def rotate(text, key):
    # 1. Input ist text (str), key (int)
    # 2. Output ist nur ein str mit rotiertem Input.
    # 3. Sonderfälle - hier diesmal keine. Sonst leerer Input oder so.
    
    letters = ("abcdefghijklmnopqrstuvwxyz") # 26 Buchstaben - 0-25 Ziffern Index.    
    rot_string = ""
    
    for original_char in text:
        if original_char.isalpha():
            is_upper = original_char.isupper()
            lower_char = original_char.lower()
            old_position = letters.index(lower_char)
            new_position = (old_position + key) % 26
            rotated_char = letters[new_position]
            if is_upper:
                rotated_char = rotated_char.upper()
        else:
            rotated_char = original_char
            
        rot_string += rotated_char
        
    return rot_string
        
            

    # Ich möchte eine Rotation - übergeben von key - durch das Alphabet machen, aber NUR für den 
    # übergebenen text-Abschnitt.


# text	Der gesamte Eingabetext, den du rotieren willst.
# key	Die Zahl, um die jeder Buchstabe verschoben werden soll.
# letters (früher alphabet)	Der String "abcdefghijklmnopqrstuvwxyz", alle Buchstaben in Reihenfolge.
# rot_string	Der String, in dem nach und nach die rotierten Buchstaben gesammelt werden.
# original_char (früher ch)	Der aktuelle Buchstabe aus text, den du gerade bearbeitest.
# is_upper	Boolean (True/False), speichert, ob original_char großgeschrieben war.
# old_position	Der Index von original_char im Alphabet (letters). Beispiel: 'c' → 2.
# new_position	Der Index nach Rotation: (old_position + key) % 26.
# rotated_char (früher new_ch)	Der Buchstabe nach der Rotation, evtl. in Großbuchstaben umgewandelt.