#!/usr/bin/env python3
import sys
import re

class fgPolicyRouteObject(object):
    def __init__(self, id=None):
        self.number = ""
        self.input_device = ""
        self.srcaddr = ""
        self.dst = ""
        self.dstaddr = ""
        self.gateway = ""
        self.output_device = ""
        self.action = ""
        self.protocol = ""
        self.start_port = ""
        self.end_port = ""


in_local_fwobject = 0
in_edit_fwobject = 0

header = "number;input-device;srcaddr;dst;dstaddr;gateway;output-device;action;protocol;start-port;end-port"
print(header)

if __name__ == '__main__':
    fd = open(sys.argv[1], 'r')
    line = fd.readline()

    for line in fd.readlines():
        cnf = line.strip()
        if cnf == "config router policy":
            in_local_fwobject = 1
            print("Parsing policy routes")
            continue
        if cnf.startswith("edit"):
            in_edit_fwobject = 1
            fwobject = fgPolicyRouteObject()
            fwobject.number = cnf.split(" ")[1]
            fwobject.number = fwobject.number.replace('"', '')
        if cnf.startswith("set input-device"):
            fwobject.input_device = cnf.split(" ")[2]
        if cnf.startswith("set output-device"):
                    fwobject.output_device = cnf.split(" ")[2]
        if cnf.startswith("set srcaddr "):
            fwobject.srcaddr = cnf.split(" ")[2]
        if cnf.startswith("set dstaddr "):
            fwobject.dstaddr = re.sub('set ', '', cnf)
        if cnf.startswith("set dst "):
            fwobject.dst = cnf.split(" ")[2]
        if cnf.startswith("set gateway"):
            fwobject.gateway = cnf.split(" ")[2]
        if cnf.startswith("set output-device"):
            fwobject.output_device = cnf.split(" ")[2]
        if cnf.startswith("set action"):
            fwobject.action = cnf.split(" ")[2]
        if cnf.startswith("set protocol"):
            fwobject.protocol = cnf.split(" ")[2]
        if cnf.startswith("set start-port"):
            fwobject.start_port = cnf.split(" ")[2]
        if cnf.startswith("set end-port"):
            fwobject.end_port = cnf.split(" ")[2]
        if cnf.startswith("next"):
            id_edit_fwobject = 0
            csvline = fwobject.number + ";" + fwobject.input_device + ";" + fwobject.srcaddr + ";" + fwobject.dst + ";" + fwobject.dstaddr + ";" + fwobject.gateway + \
                ";" + fwobject.output_device + ";" + fwobject.action + ";" + \
                fwobject.protocol + ";" + fwobject.start_port + ";" + fwobject.end_port + ";"
            print(csvline)
            continue
        else:
            continue
