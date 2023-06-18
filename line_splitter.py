def line_splitter(line): #Function used with words with etimology to checks their type and gender
    if "ad. m. f." in line[1]:
        return "Adjetivo","Masculino e Feminino"
    elif "ad. m." in line[1]:
        return "Adjetivo","Masculino"
    elif "ad. f." in line[1]:
        return "Adjetivo","Feminino"
    elif "ad. n." in line[1]:
        return "Adjetivo","Neutro"
    elif "ad." in line[1]:
        return "Adjetivo",""
    elif "adv." in line[1]:
        return "Adverbio",""
    elif "s. m. f." in line[1]:
        return "Substantivo","Masculino e Feminino"
    elif "s. m." in line[1]:
        return "Substantivo","Masculino"
    elif "s. f." in line[1]:
        return "Substantivo","Feminino"
    elif "s. n." in line[1]:
        return "Substantivo","Neutro"
    elif "s." in line[1]:
        return "Substantivo", ""
    elif "intr." in line[1]:
        return "Verbo","Intransitivo"
    elif "tr." in line[1]:
        return "Verbo","Transitivo"
    else:
        return line
