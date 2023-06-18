# DicionarioGrego - Python Program for Data Input

<div>
  <img src="http://ForTheBadge.com/images/badges/made-with-python.svg"/>
</div>
<div>
  <img src="https://img.shields.io/badge/Kibana-005571?style=for-the-badge&logo=Kibana&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>

## About the project
The goal of this particular project is to create a digitalized version of an old but yet important Greek-Portuguese Dictionary(Dicionário Grego-Português, Isidro Pereira 8° ed). TesseractOCR will be use to generate input from the scanned pages of the dictionary, the input will be go through a trained and sofisticated algorythm to set the word parameters, such as name, etimology, type, gender, meaning, inflection.

After that a python library will be use to load the data into a database, the data can also be displayed in JSON format for a better visualization and/or metrics in Kibana for example.

## Input
This is a snippet of an scanned page of the dictionary.
<div>
  <img src="https://dicionariogrego.com/assets/images/dicionario.png"/>
</div>

## Output
This is a JSON extract from the database.
```json
{
  "id": 24497,
  "searchable": "φιλοσοφια",
  "name": "Φιλοσοφία, ας",
  "etimology": "(φιλόσοφος)",
  "type": "Substantivo",
  "gender": "Feminino",
  "meaning": " amor da ciência, estudo de uma matéria, cultura intelectual | cultivo metódico da eloquência ou da ciência das coisas, filosofia",
  "inflection": null,
  "observation": null
}
```
## Model
Everything start in the **file_reader** function, the goal of this fuction is to set the name, the searchable (name without the diacritics),
and the so called **new_line**, that's where the gender, type meaning and inflection will be, but because it contains a significant amount of condtions 
they will be treated by different functions in the program.
```python
import os 

dir_path = os.chdir(f"/home/path_to_folder")
list = []
listFiles = []
allData = []

debugger = {"Index": "", "Line": "",}

count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
print('File Count:', count)

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
```
## Kibana Metrics for the data

This is a screenshot of the a Kibana dashboard developed to illustrate and display the data in a more digestible way.

<div>
	<img src="https://res.cloudinary.com/dsques4uz/image/upload/v1687102353/kibana_sylvur.png"/>
</div>
