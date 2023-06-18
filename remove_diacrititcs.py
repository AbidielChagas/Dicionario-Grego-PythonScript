from diacritcs import diacritics

def remove_diacritics(word): #Remove diacritics from key, making words typo free and searchable
    word = word.split(",",1)
    new_word = word[0].replace("-","")
    if("(" or ")" in new_word):
        new_word = new_word.replace(")", "")
        new_word = new_word.replace("(", "")
    
    prev = new_word.replace("*", "")
    mod = str(prev)

    output = []
    i = 0
    for x in mod:
        if mod[i] in diacritics:
            output.append(diacritics.get(mod[i])) #Gets value of the given key passed by the index of input
            i += 1
        else:
            output.append(mod[i])
            i+=1
    final = "".join(output)
    return final.lower() #Return the seachable term in lowercase.