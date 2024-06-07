from colorama import Fore, Back, Style

internalError = Fore.RED + '''An internal Error occured. Restart the program or try again. Error signature: ''' + Style.RESET_ALL

lineSeperator = '''-----------------------------------------------------------------------------C'''

linePrompt = Back.LIGHTBLUE_EX + Fore.BLACK + '''>>> ''' + Style.RESET_ALL

abortKeyword = '''abort'''

confirmKeyword = '''CONFIRM'''

insertIDnotValid = '''Your chosen ID is not valid (already taken or other violation)'''

idPrompt = '''id='''

contentPrompt = '''content='''

deadlinePrompt = '''deadline='''

initWarning = Fore.RED + '''WARNING THIS WILL DELETE ALL YOUR NOTES!!! DO YOU WANT TO CONTINUE?''' + Style.RESET_ALL

typeConfirmWarning = '''Type <CONFIRM> to confirm the operation'''

commandNotRecognized = Fore.LIGHTRED_EX + '''Command not recognized! type <help> for more''' + Style.RESET_ALL

helpMessage = '''
    This is the todl program writen by Franzisco Schmidt 

    It is used to store and handle very simple todo-list actions through a command
    line interface. Use commands to interface with the program:

    <help> - prints this message
    <init files> - writes the files 'done' and 'todo' new
    <list all> - lists all entries in both files
    <list done> - lists entries in 'done'
    <list todo> - lists entries in 'todo'
    <insert> - insert an item into the list (this will open another prompt)
    <did> - change the status of the entry with id=param to done (this will open another prompt)
    <undid> - change the status of the entry with id=param to todo (this will open another prompt)
    <delete done> - removes all entries in 'done'
    <exit> - closes the program

'''

startedSession = '''Starting session...'''

endingSession = '''Have a good one!'''

