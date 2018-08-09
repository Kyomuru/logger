# logger
Simple logger project in python

This is a simple logger module for python, is really simple to use.
in this version the log.txt file will be created on desktop, for change the directory you can open the file with some python ide and change the directory (dir_l var).

Here you can find a short guide about all func:

general_log(text): This func will write on the logs file with the string or string variable, like this:

general_log("hi!") ---> [here you can find the date and time] >> hi!
__________________________________________________________________________________________________________________________________________
var_changed(var, namevar): This func will report name of the variable and the actual value, like this:

num = 26

var_changed(num, name_of_num) ---> [here you can find the date and time] >> value of num changed in 26
__________________________________________________________________________________________________________________________________________
process(command): This func will print in the logs, depending to the command, "program start" or "program close", you use this func like this:

process("start") ---> [here you can find the date and time] >> programm start

process("close") ---> [here you can find the date and time] >> programm close

P.S. if you use  the command: close the file of the logs will be automatically closed! use only at the end of the program!
__________________________________________________________________________________________________________________________________________
cfg_menu(): Enter the configuration menu directly in the process.
__________________________________________________________________________________________________________________________________________
send_email(): Send an email with the logs, you can change the parameters of email in the file logconf.txt or directly in the process using the previous command.
