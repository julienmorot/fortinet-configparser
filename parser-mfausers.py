#!/usr/bin/env python
import sys


class fgUser(object):
	def __init__(self,id=None):
		self.name = ""
                self.type = ""
		self.mfa = ""
		self.email = ""
		self.sms = ""
		self.fortitoken = ""

in_local_user = 0
in_edit_user = 0

header="name;type;mfa;sms;email;fortitoken"
print(header)

if __name__ == '__main__':
#	fd = open(sys.argv[1],'r')
        fd = open('config.txt')
	line = fd.readline()

	for line in fd.readlines():
                cnf = line.strip()
		if  cnf == "config user local":
			in_local_user = 1
			print("Parsing user config")
			continue
                if cnf.startswith("edit"):
                    	in_edit_user = 1
                    	user = fgUser()
                    	user.name =  cnf.split(" ")[1]
			user.name = user.name.replace('"','')
		if cnf.startswith("set two-factor"):
			user.mfa = cnf.split(" ")[2]
                if cnf.startswith("set email-to"):
                        user.email = cnf.split(" ")[2]
			user.email = user.email.replace('"','')
                if cnf.startswith("set sms-phone"):
                        user.sms = cnf.split(" ")[2]
			user.sms = user.sms.replace('"','')
                if cnf.startswith("set fortitoken"):
                        user.fortitoken = cnf.split(" ")[2]
			user.fortitoken = user.fortitoken.replace('"','')
                if cnf.startswith("set type"):
                        user.type = cnf.split(" ")[2]
                if cnf.startswith("next"):
                    	id_edit_user =0
			csvline = user.name + ";" + user.type + ";" + user.mfa + ";" + user.sms + ";" + user.email + ";" + user.fortitoken
			print(csvline)
                    	continue
		else:
			continue
