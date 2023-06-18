def verb_setter(meaning): #Checks if a word meaning has inflection if so it generates a new schema and appends it to the map.
    if "/(" in meaning:
        return meaning.split("/", 1)
    else:
        return meaning