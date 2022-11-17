from abc import ABC, abstractmethod
import time

class baseLog(ABC):

    #static
    logName: str = ''
    logFilePath: str = ''
    logFile = None
    bOverwriteLog: bool = False
    buffer = ''

    def staticInit( filePath, fileName, overWriteLog = False):
        baseLog.logFilePath = filePath
        baseLog.bOverwriteLog = overWriteLog
        baseLog.logName = fileName
        if baseLog.bOverwriteLog == True:
            baseLog.logName += ".txt"
            baseLog.loadFile('w+')
            baseLog.flushFile()
            baseLog.buffer = baseLog.logFile.read()
        else:
            baseLog.logName = fileName + logUtils.logCTimeFix(time.ctime()) + ".txt"
            baseLog.logName = logUtils.logFileNameFix(baseLog.logName)
            baseLog.loadFile('w+')
            baseLog.buffer = baseLog.logFile.read()

    def setLogFilePath(inLogFilePath):
        baseLog.logFilePath = inLogFilePath

    def loadFile(mode):
        baseLog.logFile = open(baseLog.logFilePath + baseLog.logName, mode)

    def flushFile():
        baseLog.logFile.write('')

    def closeFile():
        baseLog.logFile.close()

    #static end

    def __init__(self, bUseTime = True, bSilent = False):
        self.prefix = "Base. "
        self.msg = 'base message '
        self.postData = "post data "
        self.bUseTime = bUseTime
        self.bSilent = bSilent

    @abstractmethod
    def write():
        pass


    def printConsole(self):
        if self.bSilent == False:
            print(self.prefix, self.msg, self.postData)
    
    def printFile(self):
        if self.bUseTime == True:
            self.buffer = self.buffer + '\n'
            self.buffer = self.buffer + time.ctime()
            self.buffer = self.buffer + ' '
        else:
            self.buffer = self.buffer('\n')

        self.buffer = self.buffer + self.prefix
        self.buffer = self.buffer + self.msg
        self.buffer = self.buffer + self.postData
        self.logFile.write(self.buffer)

    def flushFile(self):
        baseLog.flushFile()
    
    

    
class debugLog(baseLog):

    def __init__(self, msg, dataMsg = '', bPrintFile = False):
        baseLog.__init__(baseLog)
        self.prefix = "Debug. "
        self.msg = msg
        self.postData = dataMsg
        self.bPrintFile = bPrintFile
        self.write()

    def write(self):
        self.printConsole()
        if self.bPrintFile is True: self.printFile()

class warningLog(baseLog):

    def __init__(self, msg, dataMsg = ''):
        baseLog.__init__(baseLog)
        self.prefix = "Warning. "
        self.msg = msg
        self.postData = dataMsg
        self.write()

    def write(self):
        self.printConsole()
        self.printFile()

class errorLog(baseLog):

    def __init__(self, msg, dataMsg = ''):
        baseLog.__init__(baseLog)
        self.prefix = "Error. "
        self.msg = msg
        self.postData = dataMsg
        self.write()

    def write(self):
        self.printConsole()
        self.printFile()

class simpleLog(baseLog):

    def __init__(self, msg, dataMsg = '', bPrintFile = False):
        baseLog.__init__(baseLog,False, False)
        self.prefix = "Log. "
        self.msg = msg
        self.postData = dataMsg
        self.bPrintFile = bPrintFile
        self.write()

    def write(self):
        self.printConsole()
        if self.bPrintFile is True: self.printFile()

class logUtils():
    
    def logCTimeFix(ctime: str):
        exceptChars = [':']
        for char in exceptChars:
            ctime = ctime.replace(char, '')
        return ctime

    def logFileNameFix(logName: str):
        exceptChars = [' ']
        for char in exceptChars:
            logName = logName.replace(char, '_')
        return logName