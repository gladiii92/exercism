# Definiere das Alphabet (klar und modular)
PLAIN = 'abcdefghijklmnopqrstuvwxyz1234567890'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba1234567890'

def encode(plain_text: str) -> str:
    """
    Verschlüsselt einen Text mit einem einfachen Substitutionscipher.
    Nicht im Alphabet enthaltene Zeichen werden ignoriert.
    Das Ergebnis wird in 5er-Blöcken zurückgegeben.
    """
    # Schritt 1: Text in das Cipher übersetzen
    encoded_chars = [
        CIPHER[PLAIN.index(char.lower())]
        for char in plain_text
        if char.lower() in PLAIN
    ]
    # Schritt 2: Liste von Zeichen zu String zusammenfügen
    encoded_string = "".join(encoded_chars)

    # Schritt 3: In 5er-Blöcke aufteilen
    block_size = 5
    return " ".join(
        encoded_string[i:i + block_size] 
        for i in range(0, len(encoded_string), block_size)
    )
def decode(ciphered_text: str) -> str:
    """
    Entschlüsselt einen verschlüsselten Text, der mit encode erzeugt wurde.
    Nicht im Cipher enthaltene Zeichen werden ignoriert.
    """
    # Schritt 1: Jedes Zeichen zurück in den Klartext übersetzen
    return "".join(
        PLAIN[CIPHER.index(char.lower())]
        for char in ciphered_text
        if char.lower() in CIPHER
    )