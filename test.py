#!/usr/bin/python3

import subprocess as sp
import imaplib
import email
import email.parser
import mailparser
import getpass
import time
import cv2

dataup=[]
ask= input("IS THIS THE FIRST SCRIPT RUN [Y/N] ? \t")
if ask == "Y" or ask == "y":
    seek = "ALL"
elif ask =="n" or ask == "N":
    seek = "UNSEEN"
else:
    exit()
mail = imaplib.IMAP4_SSL('imap.gmail.com')

aka = input('Do You Want to change Mail ID [Y/N] ? \t')

if aka == "Y" or aka == "y":
    new_m = input("Enter New Mail_ID:\t")
    new_p = getpass.getpass("Enter the App Password for this account:\t")
    mail.login(new_m, new_p)
elif  aka =="N" or aka =='n':
    mail.login('aditya.m@caratlane.com', 'zxhdqilbgcshcmbv')
else:
    exit()

while (ask=="N" or ask=="n"):
    mail.list() 
    mail.select('inbox')
    result, data = mail.uid('search', None, "{}".format(seek))
    
    i = len(data[0].split()) 
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
       
        raw_email = email_data[0][1]
        mail1 = mailparser.parse_from_bytes(raw_email)
        raw_email_string = raw_email.decode('utf-8')
        
        import email.parser

        email = email.parser.Parser().parsestr(str(raw_email_string))

        fr=(email.get('From'))
        t=(email.get('To'))
        s=(email.get('Subject'))
        a = (mail1.body.splitlines())
        dataup = a[:-2]
        def convert(dataup): 
            new=""   
            for x in dataup: 
                new += x+'\n'   
            return new
        datad= convert(dataup)

        sep = '--- mail_boundary ---'
        rest = datad.split(sep, 1)[0]
        sep1 = '[image: Mailtrack]'
        rest1 = rest.split(sep1, 1)[0]
        sep2 = '<!DOCTYPE html'
        rest2 = rest1.split(sep2, 1)[0]
        sep3 = '<https:'
        rest3= rest2.split(sep3, 1)[0]


        def get_var_value(filename="varstore.dat"):
            with open(filename, "a+") as f:
                f.seek(0)
                val = int(f.read() or 0) + 1
                f.seek(0)
                f.truncate()
                f.write(str(val))
                return val

        fcounter = get_var_value()
        f = open("/home/aditya/Desktop/python/caratlane-project/mails/file{}.py".format(fcounter),"w+")
        f.write("""globvar1 = 0
globvar2 = 0
globvar3 = 0
globvar4 = 0
globvar5 = 0
def set_globvar_to_one():
	global globvar1
	globvar1 = '''{}'''
def set_globvar_to_two():
	global globvar2
	globvar2 = '''{}'''
def set_globvar_to_three():
	global globvar3
	globvar3 = '''{}'''
def set_globvar_to_four():
	global globvar4
	globvar4 = '''{}'''
def set_globvar_to_five():
	global globvar5
	globvar5 = '''{}'''
set_globvar_to_one()
set_globvar_to_two()
set_globvar_to_three()
set_globvar_to_four()
set_globvar_to_five()""".format(fr,t,s,rest2,fcounter))
        f.close()
    print("\n")    
    sp.getstatusoutput("python3 /home/aditya/Desktop/python/caratlane-project/mails/s3_up.py")
    print("File Upload Process Complete!")
    sp.getoutput("rm -rf /home/aditya/Desktop/python/caratlane-project/mails/file*")
    sp.getstatusoutput("python3 /home/aditya/Desktop/python/caratlane-project/mails/s3_down.py")
    print("File Download Process Complete!")
    sp.getstatusoutput("python3 /home/aditya/Desktop/python/caratlane-project/mails/db.py")
    print("Dashboard Upload Process Complete!")
    sp.getoutput("rm -rf /home/aditya/Desktop/python/caratlane-project/mails/file*")
    time.sleep(30)

while (ask=="Y" or ask=="y"):
    mail.list() 
    mail.select('inbox')
    result, data = mail.uid('search', None, "{}".format(seek))
       
    i = len(data[0].split()) 
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
       
        raw_email = email_data[0][1]
        mail1 = mailparser.parse_from_bytes(raw_email)
        raw_email_string = raw_email.decode('utf-8')
        
        import email.parser

        email = email.parser.Parser().parsestr(str(raw_email_string))

        fr=(email.get('From'))
        t=(email.get('To'))
        s=(email.get('Subject'))
        a = (mail1.body.splitlines())
        dataup = a[:-2]
        def convert(dataup): 
            new=""   
            for x in dataup: 
                new += x+'\n'   
            return new
        datad= convert(dataup)

        sep = '--- mail_boundary ---'
        rest = datad.split(sep, 1)[0]
        sep1 = '[image: Mailtrack]'
        rest1 = rest.split(sep1, 1)[0]
        sep2 = '<!DOCTYPE html'
        rest2 = rest1.split(sep2, 1)[0]
        sep3 = '<https:'
        rest3= rest2.split(sep3, 1)[0]


        def get_var_value(filename="varstore.dat"):
            with open(filename, "a+") as f:
                f.seek(0)
                val = int(f.read() or 0) + 1
                f.seek(0)
                f.truncate()
                f.write(str(val))
                return val

        fcounter = get_var_value()
        f = open("/home/aditya/Desktop/python/caratlane-project/mails/file{}.py".format(fcounter),"w+")
        f.write("""globvar1 = 0
globvar2 = 0
globvar3 = 0
globvar4 = 0
globvar5 = 0
def set_globvar_to_one():
    global globvar1
    globvar1 = '''{}'''
def set_globvar_to_two():
    global globvar2
    globvar2 = '''{}'''
def set_globvar_to_three():
    global globvar3
    globvar3 = '''{}'''
def set_globvar_to_four():
    global globvar4
    globvar4 = '''{}'''
def set_globvar_to_five():
    global globvar5
    globvar5 = '''{}'''
set_globvar_to_one()
set_globvar_to_two()
set_globvar_to_three()
set_globvar_to_four()
set_globvar_to_five()""".format(fr,t,s,rest2,fcounter))
        f.close()
    break

print("\n\n")    
sp.getstatusoutput("python3 /home/aditya/Desktop/python/caratlane-project/mails/s3_up.py")
print("File Upload Process Complete!")
sp.getoutput("rm -rf /home/aditya/Desktop/python/caratlane-project/mails/file*")
sp.getstatusoutput("python3 /home/aditya/Desktop/python/caratlane-project/mails/s3_down.py")
print("File Download Process Complete!")
sp.getstatusoutput("python3 /home/aditya/Desktop/python/caratlane-project/mails/db.py")
print("Dashboard Upload Process Complete!")
sp.getoutput("rm -rf /home/aditya/Desktop/python/caratlane-project/mails/file*")
time.sleep(30)