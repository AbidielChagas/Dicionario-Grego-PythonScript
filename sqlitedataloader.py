from reader import list
from sqlite3 import connect

con = connect('/home/path_to_folder/data.db')
cur = con.cursor()

def sqlite_dataloader(): #Loads data to sqlite from an array of dictionaries
    dict = {}
    for i in range(0, len(list)):
        dict = list[i]
        if 'inflection' in dict:
            cur.execute("INSERT INTO Words (Id, SEARCHABLE,NAME,ETIMOLOGY,TYPE,GENDER,INFLECTION,OBSERVATION,MEANING) VALUES (?,?,?,?,?,?,?,?,?)",(None, dict.get("searchable"), dict.get("name"), dict.get("etimology"), dict.get("type"), dict.get("gender"), dict.get("inflection"), "", dict.get("meaning")));
        elif 'observation' in dict:
            cur.execute("INSERT INTO Words (Id, SEARCHABLE,NAME,ETIMOLOGY,TYPE,GENDER,INFLECTION,OBSERVATION,MEANING) VALUES (?,?,?,?,?,?,?,?,?)",(None, dict.get("searchable"), dict.get("name"), dict.get("etimology"), dict.get("type"), dict.get("gender"), "", dict.get("observation"), dict.get("meaning")));
        elif 'inflection' and 'observation' in dict:
            cur.execute("INSERT INTO Words (Id, SEARCHABLE,NAME,ETIMOLOGY,TYPE,GENDER,INFLECTION,OBSERVATION,MEANING) VALUES (?,?,?,?,?,?,?,?,?)",(None, dict.get("searchable"), dict.get("name"), dict.get("etimology"), dict.get("type"), dict.get("gender"), dict.get("inflection"), dict.get("observation"), dict.get("meaning")));
        else:
            cur.execute("INSERT INTO Words (Id, SEARCHABLE,NAME,ETIMOLOGY,TYPE,GENDER,INFLECTION,OBSERVATION,MEANING) VALUES (?,?,?,?,?,?,?,?,?)",(None, dict.get("searchable"), dict.get("name"), dict.get("etimology"), dict.get("type"), dict.get("gender"), "", "", dict.get("meaning")));

    con.commit()
    print("Record inserted successfully")
    con.close()
