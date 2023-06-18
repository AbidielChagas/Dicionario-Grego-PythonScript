import os, json
from reader import list, letter

def file_writer(): #Write to file the NDJSON schema
    os.chdir(f"/home/deb/Desktop/PR/Finals/{letter}")
    filename = f"{letter}.txt"

    out = open(filename, 'w')

    for i in range(0, len(list)):
        # print(list[i])
        out.write(str(list[i]))
        out.write('\n')
        i += 1 

    out.close()

def json_writer():
    jsonStr = json.dumps(list, indent=4, ensure_ascii=False)

    with open("sample.json", "w", encoding='utf-8') as outfile:
        outfile.write(jsonStr)
