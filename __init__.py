### PYLOG ###
## IMPORTS ##
import time
from datetime import datetime

# create mod file
try:
    open("mod.txt", "r")
except:
    open("mod.txt", "x")

## COLOURS DEFINE ##
class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

## ERROR CLASS ##
# for people who use VSCode auto complete lol
class level:
    done = "DONE"
    warn = "WARNING"
    info = "INFO"
    error = "ERROR"
    fail = "FAIL"
    exit = "EXIT"

## LOG ##
def log(message, msg_error=level.info):
    message_state = ["",""]
    message_state[0] = str(datetime.now().strftime('%H:%M:%S'))
    message_state[1] = message

    if msg_error=="DONE":
        colour = colours.OKGREEN
    elif msg_error=="WARNING":
        colour = colours.WARNING
    elif msg_error=="INFO":
        colour = colours.OKCYAN
    elif msg_error=="ERROR" or "FAIL" or "EXIT":
        colour = colours.FAIL
    
    message_structure=message_state[0]+" -- "+"("+colour+msg_error+colours.ENDC+") "+colour+message_state[1]+colours.ENDC
    print(message_structure)
    message_structure=message_state[0]+" -- "+"("+msg_error+") "+message_state[1]
    mod=open("mod.txt","a")
    mod.write(message_structure+"\n")

## ASK ##
def ask(message):
    message_state = ["",""]
    global name
    msg_error = "INPUT"
    colour = colours.OKBLUE
    message_state[0] = str(datetime.now().strftime('%H:%M:%S'))
    message_state[1] = message
    message_structure=message_state[0]+" -- "+"("+colour+msg_error+colours.ENDC+") "+colour+message_state[1]+colours.ENDC+"\n"
    answer = input(message_structure)
    message_structure=message_state[0]+" -- "+"("+msg_error+") "+message_state[1]+"\n"
    mod=open("mod.txt","a")
    mod.write(message_structure+answer+"\n")
    mod.close()
    return answer