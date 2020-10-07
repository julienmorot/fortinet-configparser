#!/usr/bin/env python
import sys
import re


class fgFwGrp(object):
	def __init__(self,id=None):
		self.name = ""
                self.member = ""

in_local_fwgrp = 0
in_edit_fwgrp = 0

header="name;member"
print(header)

if __name__ == '__main__':
	fd = open(sys.argv[1],'r')
	line = fd.readline()

	for line in fd.readlines():
                cnf = line.strip()
		if  cnf == "config firewall addrgrp":
			in_local_fwgrp = 1
			print("Parsing firewall groups")
			continue
                if cnf.startswith("edit"):
                    	in_edit_fwgrp = 1
                    	fwgrp = fgFwGrp()
                    	fwgrp.name =  cnf.split(" ")[1]
			fwgrp.name = fwgrp.name.replace('"','')
		if cnf.startswith("set member"):
                    fwgrp.member = re.sub('set member', '', cnf)
                if cnf.startswith("next"):
                    	id_edit_fwgrp =0
			csvline = fwgrp.name + ";" + fwgrp.member + ";"
			print(csvline)
                    	continue
		else:
			continue
