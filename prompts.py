
internalError = '''An internal Error occured. Restart the program or try again. Error signature: '''

lineSeperator = '''-----------------------------------------------------------------------------C'''

linePrompt = '''>>>'''

insertIDask = '''Enter the entry ID'''

insertIDnotValid = '''Your chosen ID is not valid (already taken or other violation)'''

insertContent = '''Enter the content of your new entry'''

commandNotRecognized = '''Command not recognized! type <help> for more'''

helpMessage = '''
    This is the todolist program writen by Franzisco Schmidt 

    It is used to store and handle very simple todo-list actions through a command
    line interface. Use commands to interface with the program:

    <help> - prints this message
    <init files> - writes the files 'done' and 'todo' new if they dont exist
    <list all> - lists all entries in both files
    <list done> - lists entries in 'done'
    <list todo> - lists entries in 'todo'
    <insert> - insert an item into the list (this will open another prompt)
    <did> + param - change the status of the entry with id=param to done
    <undid> + param - change the status of the entry with id=param to todo
    <delete done> - removes all entries in 'done'
    <exit> - closes the program

'''

startedSession = '''Starting session...'''

