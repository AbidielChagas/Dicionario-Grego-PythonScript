from alphabet import alphabet
from diacritcs import diacritics

def line_reader(line): #Checks if word has etimology and sets word type and gender
    if line[1] in alphabet.values() and "))." in line or line[1] in diacritics.keys() and "))." in line:
        return line.split(").", 1)
    elif line[1] in alphabet.values() and ".," in line or line[1] in diacritics.keys() and "-," in line:
        line = line.replace(").", ")).")
        return line.split(").", 1)
    elif line[1] in alphabet.values() and "-," in line or line[1] in diacritics.keys() and ".," in line:
        line = line.replace(").", ")).")
        return line.split(").", 1)
    elif line[1] in alphabet.values() and ".)." in line or line[1] in diacritics.keys() and ".)." in line:
        line = line.replace(").", ")).")
        return line.split(").", 1)
    elif line[1] in alphabet.values() and "))." not in line or line[1] in diacritics.keys() and "))." not in line:
        return line.split(".", 1)
    elif 's. n.' in line:
        return line.split(".", 2)
    elif 's. m. f' in line:
        return line.split(".", 3)
    elif 's. f.' in line:
        return line.split(".", 2)
    elif 's. m.' in line:
        return line.split(".", 2)
    elif 'ad. m.' in line:
        return line.split(".", 2)
    elif 'ad. f.' in line:
        return line.split(".", 2)
    elif 'ad. n.' in line:
        return line.split(".", 2)
    elif 'adv.' in line:
        return line.split(".", 1)
    elif 'ad.' in line:
        return line.split(".", 1)
    else:
        return line