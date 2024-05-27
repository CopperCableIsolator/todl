import csv
from dataclasses import dataclass

@dataclass
class ListElem:
    id:str
    deadline:str
    content:str

def writeRowToList(item:ListElem):
    def f(csvfile):
        fieldnames =['id', 'deadline', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id' : item.id, 'deadline' : item.deadline, 'content' : item.content})
    return f

def writeRowsToList(items:list[ListElem]):
    def f(csvfile):
        fieldnames =['id', 'deadline', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for item in items:
            writer.writerow({'id' : item.id, 'deadline' : item.deadline, 'content' : item.content})
    return f

def readFromList ():
    def f(csvfile):    
        reader = csv.DictReader(csvfile)
        return [ListElem(i['id'], i['deadline'], i['content']) for i in reader]
    return f

def deleteList ():
    def f(csvfile):
        fieldnames =['id', 'deadline', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    return f

def csvInterfacer(filename, func, mode):
    with open(filename, mode, newline='') as csvFile:
        return func(csvFile)

