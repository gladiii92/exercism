def find(search_list: list[int], value: int) -> int:
    #Indexbereiche der Liste festlegen
    left = 0
    right = len(search_list) - 1
    
    # Solange left kleiner-gleich rechts:
    while left <= right:
        # MittelINDEX der Liste
        mid = (left + right) // 2

        # MittelWERT der Liste in current gespeichert
        current = search_list[mid]

        # Wenn aktueller MITTELWERT gleich dem Value -> returnt den MittelINDEX
        if current == value:
            return mid

        # Wenn aktueller MITTELWERT kleiner Value -> left = MittelINDEX + 1
        elif current < value:
            left = mid + 1
        # Sonst -> Rechts = MittelINDEX - 1
        else:
            right = mid - 1

    # Läuft solange durch bis left nicht mehr kleiner-gleich right -> Dann ValueError!
    raise ValueError("value not in array")
    
    
            
            
        