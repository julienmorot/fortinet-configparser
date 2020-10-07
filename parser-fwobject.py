#!/usr/bin/env python
import sys


class fgFwObject(object):
	def __init__(self,id=None):
		self.name = ""
                self.subnet = ""

in_local_fwobject = 0
in_edit_fwobject = 0

header="name;subnet"
print(header)

if __name__ == '__main__':
	fd = open(sys.argv[1],'r')
	line = fd.readline()

	for line in fd.readlines():
                cnf = line.strip()
		if  cnf == "config firewall addrgrp":
			in_local_fwobject = 1
			print("Parsing firewall groups")
			continue
                if cnf.startswith("edit"):
                    	in_edit_fwobject = 1
                    	fwobject = fgFwObject()
                    	fwobject.name =  cnf.split(" ")[1]
			fwobject.name = fwobject.name.replace('"','')
		if cnf.startswith("set subnet"):
                    fwobject.subnet = cnf.split(" ")[2]
                if cnf.startswith("next"):
                    	id_edit_fwobject =0
			csvline = fwobject.name + ";" + fwobject.subnet + ";"
			print(csvline)
                    	continue
		else:
                    continue
