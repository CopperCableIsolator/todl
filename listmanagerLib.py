import datahandler
from dataclasses import dataclass
import prompts
from listmanager import Csvpackage

@dataclass
class IsKeyword():
    isKeyWord:bool
    word:str

def entryFinder(listOfEntries:list[datahandler.ListElem], id) -> datahandler.ListElem:
    for i in listOfEntries:
        if i.id == id:
            return i
    return None

def isKeywordWrapper(cmd, keyword) -> IsKeyword:
    if (cmd == keyword):
        return IsKeyword(True, cmd)
    return IsKeyword(False, cmd)

def printEntries(list:list[datahandler.ListElem]):
    for ent in list:
        print(f" <> id={ent.id} | {ent.deadline} | {ent.content}")

    
def changeStatus(srcFile, dstFile):

    id = isKeywordWrapper(input(prompts.idPrompt), prompts.abortKeyword)

    if(id.isKeyWord):
        return

    list_elem = deleteEntryFromId(srcFile, id.word)
    
    datahandler.csvInterfacer(dstFile, datahandler.writeRowToList(list_elem), 'a')

def deleteEntryFromId(file, id) -> datahandler.ListElem:

    list = datahandler.csvInterfacer(file, datahandler.readFromList(), 'r')
    
    list_elem = entryFinder(list, id)
    list.remove(list_elem)

    datahandler.csvInterfacer(file, datahandler.deleteList(), 'w')
    datahandler.csvInterfacer(file, datahandler.writeRowsToList(list), 'a')

    return list_elem













def list_all(csvpackage:Csvpackage):
    l_todo = datahandler.csvInterfacer(csvpackage.csvtodo, datahandler.readFromList(), 'r')
    l_done = datahandler.csvInterfacer(csvpackage.csvdone, datahandler.readFromList(), 'r')
    printEntries(l_todo)
    print(prompts.lineSeperator)
    printEntries(l_done) 


def list_done(csvpackage:Csvpackage):
    l_done = datahandler.csvInterfacer(csvpackage.csvdone, datahandler.readFromList(), 'r')
    printEntries(l_done)


def list_todo(csvpackage:Csvpackage):
    l_todo = datahandler.csvInterfacer(csvpackage.csvtodo, datahandler.readFromList(), 'r')
    printEntries(l_todo)

def insert(csvpackage:Csvpackage):
    l_todo = datahandler.csvInterfacer(csvpackage.csvtodo, datahandler.readFromList(), 'r')
    l_done = datahandler.csvInterfacer(csvpackage.csvdone, datahandler.readFromList(), 'r')

    validID = False
    while(not validID):
        id = isKeywordWrapper(input(prompts.idPrompt), prompts.abortKeyword)
    
        if(id.isKeyWord) :
            return
        
        if (entryFinder(l_todo, id.word) != None or entryFinder(l_done, id.word) != None):
            print(prompts.insertIDnotValid)
            continue
        validID = True
    
    deadline = isKeywordWrapper(input(prompts.deadlinePrompt), prompts.abortKeyword)

    if(deadline.isKeyWord):
        return

    content = isKeywordWrapper(input(prompts.contentPrompt), prompts.abortKeyword)
    
    if(content.isKeyWord):
        return
    
    datahandler.csvInterfacer(csvpackage.csvtodo, datahandler.writeRowToList(datahandler.ListElem(id.word, deadline.word, content.word)), 'a')


def did(csvpackage:Csvpackage):
    changeStatus(csvpackage.csvtodo, csvpackage.csvdone)

def undid(csvpackage:Csvpackage):
    changeStatus(csvpackage.csvdone, csvpackage.csvtodo)

def delete_todo(csvpackage:Csvpackage):
    id = isKeywordWrapper(input(prompts.idPrompt), prompts.abortKeyword)

    if(id.isKeyWord):
        return

    deleteEntryFromId(csvpackage.csvtodo, id.word)

def delete_done(csvpackage:Csvpackage):
    id = isKeywordWrapper(input(prompts.idPrompt), prompts.abortKeyword)

    if(id.isKeyWord):
        return

    deleteEntryFromId(csvpackage.csvdone, id.word)

def init(csvpackage:Csvpackage):
    print(prompts.initWarning)
    if(isKeywordWrapper(input(prompts.typeConfirmWarning), prompts.confirmKeyword).isKeyWord):
        datahandler.csvInterfacer(csvpackage.csvtodo, datahandler.deleteList(), 'w')
        datahandler.csvInterfacer(csvpackage.csvdone, datahandler.deleteList(), 'w')
