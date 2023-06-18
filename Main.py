from reader import file_reader
from reader import debugger
from reader import setter
from file_writer import json_writer
from dbLoader import sqlitedataloader
file_reader()
try:
    file_reader()
except:
    print("Reading: "+ str(debugger["Index"]) +" "+ str(debugger["Line"]))
    
try: 
    setter()
except:
    print("Setting: " + str(debugger["Index"]) +" "+ str(debugger["Line"]))

json_writer()
sqlitedataloader.sqlite_dataloader()