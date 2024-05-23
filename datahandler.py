import csv
from dataclasses import dataclass

@dataclass
class ListElem:
    id:str
    done:bool
    content:str

def _printRead (list):
    for i in list:
        print(i)

def writeRowToList(item:ListElem):
    def f(csvfile):
        fieldnames =['id', 'done?', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id' : item.id, 'done?': item.done, 'content' : item.content})
    return f

def writeRowsToList(items:list):
    def f(csvfile):
        fieldnames =['id', 'done?', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for item in items:
            writer.writerow({'id' : item.id, 'done?': item.done, 'content' : item.content})
    return f

def readFromList ():
    def f(csvfile):    
        reader = csv.DictReader(csvfile)
        return list(reader)
    return f

def deleteList ():
    def f(csvfile):
        fieldnames =['id', 'done?', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    return f

def csvInterfacer(filename, func, mode):
    with open(filename, mode, newline='') as csvFile:
        return func(csvFile)

