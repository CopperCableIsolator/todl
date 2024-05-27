import prompts
import listmanagerLib
from dataclasses import dataclass

head = ''
csvtodo = 'todo.csv'
csvdone = 'done.csv'


@dataclass 
class Csvpackage:
    head:str
    csvtodo:str
    csvdone:str

csvpackage = Csvpackage(head=head, csvtodo=csvtodo, csvdone=csvdone)

commandDict = {
    "list all" : 1 ,
    "list done" : 2 ,
    "list todo" : 3 ,
    "insert" : 4 ,
    "did" : 5 ,
    "delete done" : 6,
    "delete todo" : 7,
    "init" : 8,
    "undid" : 9,
    "help" : 10,
    "exit" : 11
     #DELETETODO :x
}

def awaitCommandInput():
    inp = input(prompts.linePrompt)
    if inp in commandDict:
        return commandDict.get(inp)
    else :
        print(prompts.commandNotRecognized) 
        return 0
    
def setCsvPackage(head, csvtodo, csvdone):
    csvpackage = Csvpackage(head=head, csvtodo=csvtodo, csvdone=csvdone)

def list_all():
    listmanagerLib.list_all(csvpackage)

def list_done():
    listmanagerLib.list_done(csvpackage)

def list_todo():
    listmanagerLib.list_todo(csvpackage)

def insert():
    listmanagerLib.insert(csvpackage)

def did():
    listmanagerLib.did(csvpackage)

def undid():
    listmanagerLib.undid(csvpackage)

def delete_todo():
    listmanagerLib.delete_todo(csvpackage)

def delete_done():
    listmanagerLib.delete_done(csvpackage)

def init():
    listmanagerLib.init(csvpackage)

def help():
    print(prompts.helpMessage)

def exit():
    print(prompts.endingSession)
    exit(0)



def main():
    print(prompts.startedSession)
    run = True
    while(run):
        if (i := awaitCommandInput()) != 0:
            match i :
                case 1: #list all
                    list_all()
                case 2: #list done
                    list_done()
                case 3: #list todo
                    list_todo()
                case 4: #insert
                    insert()
                case 5: #did
                    did()
                case 6: #delete done
                    delete_done()
                case 7: #delete todo
                    delete_todo() 
                case 8: #init
                    init()
                case 9: #undid
                    undid()
                case 10:
                    print(prompts.helpMessage)
                case 11:
                    print(prompts.endingSession)
                    exit(0)
                case _:
                    print(f"{prompts.internalError} main:command id not recognized")

if __name__ == "__main__":
    main()