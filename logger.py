from datetime import datetime
import getpass
from os import system, chdir, listdir
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def seecredits():
    print("""
    ============================================================================
         /$$                                                                
        | $$  by Kyomuru                                                     
        | $$        /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
        | $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
        | $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
        | $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
        |________/ \______/  \____  $$ \____  $$ \_______/|__/      
                            /$$  \ $$ /$$  \ $$                    
                            |  $$$$$$/|  $$$$$$/       logger config 1.0             
                             \______/  \______/                     
    ============================================================================                         
                             """)
    print(" Module created by Kyomuru, special thanks to Zeta|314! ")
    system("pause")

class logger(object):

    def __init__(self):
        self.user = getpass.getuser()
        self.dir_l = "C:\\Users\\{}\\Desktop\\log.txt".format(self.user)
        self.logger_file = open(self.dir_l, "w")
        self.cfg_file = open("logconf.txt","r+")
        self.cfg_actual = self.cfg_file.readlines()
        self.actual_email = self.cfg_actual[0].splitlines()[0].split(" = ")[1]
        self.actual_pass = self.cfg_actual[1].splitlines()[0].split(" = ")[1]
        self.actual_emailto = self.cfg_actual[2].splitlines()[0].split(" = ")[1]
        self.cfg_file.close()
        self.cfg_file = open("logconf.txt", "w+")


    def general_log(self, text):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> {}.\n".format(date,text))

    def var_changed(self,var,name_var):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> value of {} changed in {}\n.".format(date, name_var, str(var)))

    def process(self,command):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        if command.lower() == "start":
            self.logger_file.write("[{}]>> process start.\n".format(date))
        elif command.lower() == "close":
            self.logger_file.write("[{}]>> process close.\n".format(date))
            self.logger_file.close()
        else:
            self.logger_file.write("[{}]>> Error_01 = invalid syntax.\n".format(date))

    def cfg_menu(self):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> loading cfg menù...\n".format(date))
        chose = ""
        cfg_cont = ""
        print("\n" * 50)
        print("""
============================================================================
     /$$                                                                
    | $$  by Kyomuru                                                     
    | $$        /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
    | $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
    | $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
    | $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
    | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
    |________/ \______/  \____  $$ \____  $$ \_______/|__/      
                        /$$  \ $$ /$$  \ $$                    
                        |  $$$$$$/|  $$$$$$/       logger config 1.0             
                         \______/  \______/                     
============================================================================                         
                         """)
        while True:
         print("""
  Welcome to logger config 1.0, here you can change the following parameters: 
    1)the email where the logs will be sent from.
    2)the password of the email.
    3)the email address to whitch the logs will be sent.
  Or you can:
    4)see Credits
    5)close config  
      """)
         chose = input("insert the number of the option: ")
         try:
             if int(chose) > 5 or int(chose) < 1:
                 print("invalid chose, use only number of option!")
                 continue
         except ValueError:
             print("invalid chose, use only number of option!")
             continue

         if int(chose) == 1:
             while True:
                 print("actual email = {}\n".format(self.actual_email))
                 chose = input(
                     "insert here your email (with this version of logger you can use only gmail addres, type exit to... exit): ")
                 if chose.lower() == "exit":
                     break
                 if not chose.endswith("@gmail.com"):
                     print("you can use only gmail addres! retry \n")
                 else:
                     self.actual_email = chose
                     cfg_cont = "email = {}\n password = {}\n emailto = {}".format(self.actual_email, self.actual_pass,
                                                                                   self.actual_emailto)
                     self.cfg_file.write(cfg_cont)
                     date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
                     self.logger_file.write("[{}]>> email = {} (in logger config).\n".format(date, chose))
                     break

         elif int(chose) == 2:
             while True:
                 print("actual password = {}\n".format(self.actual_pass))
                 chose = input("insert here your password (of the email, type exit to... exit): ")
                 if chose.lower() == "exit":
                     break
                 else:
                     self.actual_pass = chose
                     cfg_cont = "email = {}\n password = {}\n emailto = {}".format(self.actual_email, self.actual_pass,self.actual_emailto)
                     self.cfg_file.write(cfg_cont)
                     date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
                     self.logger_file.write("[{}]>> password = {} (in logger config).\n".format(date, chose))
                     break

         elif int(chose) == 3:
             while True:
                 print("actual email = {}\n".format(self.actual_emailto))
                 chose = input(
                     "insert here the email address will recive the logs (with this version of logger you can use only gmail addres, type exit to... exit): ")
                 if chose.lower() == "exit":
                     break
                 if not chose.endswith("@gmail.com"):
                     print("you can use only gmail addres! retry \n")
                 else:
                     self.actual_emailto = chose
                     cfg_cont = "email = {}\n password = {}\n emailto = {}".format(self.actual_email, self.actual_pass,
                                                                                   self.actual_emailto)
                     self.cfg_file.write(cfg_cont)
                     date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
                     self.logger_file.write("[{}]>> email = {} (in logger config).\n".format(date, chose))
                     break

         elif int(chose) == 4:
             seecredits()

         elif int(chose) == 5:
             break

        if self.cfg_file.read() == "" or self.cfg_file.read() == " ":
             cfg_cont = "email = {}\n password = {}\n emailto = {}".format(self.actual_email, self.actual_pass, self.actual_emailto)
             self.cfg_file.write(cfg_cont)

        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> closing cfg menù...\n".format(date, chose))

    def send_email(self):
        date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
        self.logger_file.write("[{}]>> sending email...\n".format(date, chose))
        self.logger_file.close()
        msg = MIMEMultipart()
        msg['From'] = self.actual_email
        msg['To'] = self.actual_emailto
        msg['Subject'] = "logs"
        body = "here the logs"
        msg.attach(MIMEText(body,'plain'))

        fromaddr = self.actual_email
        password = self.actual_pass
        toaddr = self.actual_emailto
        filename = "logs.txt"

        attachment = open(self.dir_l,'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
        msg.attach(part)
        text = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        self.logger_file = open("C:\\Users\\{}\\Desktop\\log.txt".format(self.user), "w")
        cfg_cont = "email = {}\n password = {}\n emailto = {}".format(self.actual_email, self.actual_pass,self.actual_emailto)
        self.cfg_file.write(cfg_cont)

































