import re

def logParser():
    file = open("log.txt", "r")
    logFile= file.read()
    file.close()
    listLines = re.split('\n',logFile)
    output = open("outputLog.txt", "w") 
    for i in listLines:
        if('[Error]' in i or '[Warning]' in i) :
            output.write(i+"\n")
    output.close()

logParser()
