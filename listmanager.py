import datahandler
import prompts

commandDict = {
    "list all" : 1 ,
    "list done" : 2 ,
    "list todo" : 3 ,
    "insert" : 4 ,
    "did" : 5 ,
    "delete done" : 6,
    "delete todo" : 7,
    "init" : 8 ,
    "undid" : 9
    #DELETETODO :x
}

def printEntries(list:list):
    for ent in list:
        print(f"id={ent['id']} | {"DONE" if ent['done?'] else "TODO"} | {ent['content']}")

def insert():
    l_todo = datahandler.csvInterfacer('todo.csv', datahandler.readFromList(), 'r')
    l_done = datahandler.csvInterfacer('done.csv', datahandler.readFromList(), 'r')

    validID = False
    while(not validID):
        print(prompts.insertIDask)
        id = input(prompts.linePrompt)
        for i in l_todo:
            if i['id'] == id:
                print(prompts.insertIDnotValid)
                continue
        for i in l_done:
            if i['id'] == id:
                print(prompts.insertIDnotValid)
                continue
        validID = True
    print(prompts.insertContent)
    content = input(prompts.linePrompt)
    
    datahandler.csvInterfacer('todo.csv', datahandler.writeRowToList(datahandler.ListElem(id, False, content)))

def awaitInput(insert:bool):
    inp = input(prompts.linePrompt)
    if inp in commandDict:
        return commandDict.get(inp)
    else :
        print(prompts.commandNotRecognized) 
        return 0

def main():
    print(prompts.startedSession)
    run = True
    while(run):
        if i := awaitInput() != 0:
            match i :
                case 1:
                    l_todo = datahandler.csvInterfacer('todo.csv', datahandler.readFromList(), 'r')
                    l_done = datahandler.csvInterfacer('done.csv', datahandler.readFromList(), 'r')
                    printEntries(l_todo)
                    print(prompts.lineSeperator)
                    printEntries(l_done)
                    continue 
                case 2:
                    l_done = datahandler.csvInterfacer('done.csv', datahandler.readFromList(), 'r')
                    printEntries(l_done)
                case 3:
                    l_todo = datahandler.csvInterfacer('todo.csv', datahandler.readFromList(), 'r')
                    printEntries(l_todo)
                case 4:
                    insert() 
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass 
                case 8:
                    pass
                case 9:
                    pass
                case _:
                    print(f"{prompts.internalError} main:command id not recognized")

if __name__ == "__main__":
    main()