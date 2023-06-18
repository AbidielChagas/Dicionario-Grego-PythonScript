import os
import fnmatch
from remove_diacrititcs import remove_diacritics
from verb_setter import verb_setter
from line_splitter import line_splitter
from verb_setter import verb_setter
from line_reader import line_reader
from alphabet import alphabet
from diacritcs import diacritics

list = []
listFiles = []
allData = []

debugger = {"Index": "", "Line": "",}

letter = "ALPHA"
dir_path = os.chdir(f"/home/path_to_folder/{letter}")

count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
print('File Count:', count)

for i in range(0, count):
	listFiles.append(f"00{i}.txt")

def file_reader():
	for file in listFiles:
		debugger["Index"] = "File " + file
		lines = open(file, 'r').readlines()
		filedata = {}
		filedata['name'] = file
		filedata['key'] = ""
		filedata['newline'] = ""
		filedata['searchable'] = ""
		lkey = []
		lnew_line = []
		lsearchable = []

		for line in lines:
			debugger["Line"] = f"Line {line} " + line
			(key, value) = line.split(".", 1)
			lkey.append(key)
			searchable = remove_diacritics(key)
			lsearchable.append(searchable)
			if '*' in searchable:
				searchable = searchable.replace("*", "")
			if '\n' in value:
				new_value = value.replace("\n", "")
				new_line = line_reader(new_value)
				lnew_line.append(new_line)
			filedata['key'] = lkey;
			filedata['newline'] = lnew_line;
			filedata['searchable'] = lsearchable;
		allData.append(filedata)
 
def setter():
	for j in range (0, count):
		for i in range (0, len(allData[j]["key"])-1):
			debugger['Index'] = allData[j]["name"]
			word = allData[j]["key"][i]
			value = allData[j]["newline"][i]
			searchable = allData[j]["searchable"][i]
	
			debugger['Line'] = str(i+1) + " " +word
	
			if len(value) == 4:  # Masculine and Feminine Nouns
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Substantivo",
					'gender': "Masculino e Feminino",
					'meaning': value[3],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "s" and value[1] == " f":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Substantivo",
					'gender': "Feminino",
					'meaning': value[2],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "s" and value[1] == " m":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Substantivo",
					'gender': "Masculino",
					'meaning': value[2],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "s" and value[1] == " n":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Substantivo",
					'gender': "Neutro",
					'meaning': value[2],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "ad" and value[1] == " m":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Adjetivo",
					'gender': "Masculino",
					'meaning': value[2],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "ad":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Adjetivo",
					'gender': "",
					'meaning': value[1],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "ad" and value[1] == "f":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Adjetivo",
					'gender': "Feminino",
					'meaning': value[2],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "ad" and value[1] == "n":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Adjetivo",
					'gender': "Neutro",
					'meaning': value[2],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0] == "adv":
				map = {
					'searchable': searchable,
					'name': word,
					'etimology': "",
					'type': "Adverbio",
					'gender': "",
					'meaning': value[1],
				}
				if "*" in word:
					map['observation'] = "Vocábulo do Novo Testamento"
				list.append(map)
			elif value[0][0] == "(" and value[0][1] in alphabet.values() or value[0][0] == "(" and value[0][1] in diacritics.keys() or "(sub." in value:
				type, gender = line_splitter(value)

				if type == "Adjetivo" and gender == "Masculino":
					meaning = str(value[1])
					meaning = meaning.replace("ad. m.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Adjetivo" and gender == "Feminino":
					meaning = str(value[1])
					meaning = meaning.replace("ad. f.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Adjetivo" and gender == "Masculino e Feminino":
					meaning = str(value[1])
					meaning = meaning.replace("ad. m. f.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Substantivo" and gender == "Masculino":
					meaning = str(value[1])
					meaning = meaning.replace("s. m.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Substantivo" and gender == "Feminino":
					meaning = str(value[1])
					meaning = meaning.replace("s. f.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Substantivo" and gender == "Masculino e Feminino":
					meaning = str(value[1])
					meaning = meaning.replace("s. m. f.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Substantivo" and gender == "Neutro":
					meaning = str(value[1])
					meaning = meaning.replace("s. n.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Adjetivo" and gender == "":
					meaning = str(value[1])
					meaning = meaning.replace("ad.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Adverbio" and gender == "":
					meaning = str(value[1])
					meaning = meaning.replace("adv.", "")
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Verbo" and gender == "Intransitivo":
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': value[1],
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				elif type == "Verbo" and gender == "Transitivo":
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': value[0],
						'type': type,
						'gender': gender,
						'meaning': value[1],
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)

				else:
					meaning = verb_setter(value[1])
					if len(meaning) == 2:
						map = {
							'searchable': searchable,
							'name': word,
							'etimology': value[0],
							'type': "Verbo",
							'gender': "",
							'inflection': meaning[1],
							'meaning': meaning[0],
						}
						if "*" in word:
							map['observation'] = "Vocábulo do Novo Testamento"
						list.append(map)
					else:
						map = {
							'searchable': searchable,
							'name': word,
							'etimology': value[0],
							'type': "",
							'gender': "",
							'meaning': meaning,
						}
						if "*" in word:
							map['observation'] = "Vocábulo do Novo Testamento"
						list.append(map)

			else:
				# Concatenates items in arrays to a string, so elastic search can recognize it as text.
				meaning = ''.join(value)
				new_meaning = verb_setter(meaning)
				if len(new_meaning) == 2:
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': "",
						'type': "Verbo",
						'gender': "",
						'inflection': new_meaning[1],
						'meaning': new_meaning[0],
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
				else:
					map = {
						'searchable': searchable,
						'name': word,
						'etimology': "",
						'type': "",
						'gender': "",
						'meaning': new_meaning,
					}
					if "*" in word:
						map['observation'] = "Vocábulo do Novo Testamento"
					list.append(map)
		j+=1
		
