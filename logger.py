from datetime import datetime
import getpass

class logger(object):
    def __init__(self):
        self.user = getpass.getuser()
        self.logger_file = open("C:\\Users\\{}\\Desktop\\log.txt".format(self.user), "w")

    def general_log(self, text):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> {}.\n".format(date,text))

    def var_changed(self,var,namevar):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> value of {} changed in {}.\n".format(date, namevar, str(var)))

    def process(self,command):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        if command.lower() == "start":
            self.logger_file.write("[{}]>> process start.\n".format(date))
        elif command.lower() == "close":
            self.logger_file.write("[{}]>> process close.\n".format(date))
            self.logger_file.close()
        else:
            self.logger_file.write("[{}]>> Error_01 = invalid syntax.\n".format(date))





