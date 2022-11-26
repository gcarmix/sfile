#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from libsfile import analysis

def main():
    if len(sys.argv) < 2:
        print('Error, at least 2 arguments needed')
        exit(-1)

    filename = sys.argv[1]

    fileobj = analysis.analyzeFile(filename)

    if 'md5' not in fileobj:
        print("Error analyzing file")
        sys.exit(-1)

    print("MD5 HASH:\t\t" + fileobj['md5'])
    print("SHA1 HASH:\t\t" + fileobj['sha1'])
    print("Size: \t\t\t" + str(fileobj['size']) + " bytes")
    print("Mime type:\t\t" + fileobj['mime'])
    print("Description: \t\t" + fileobj['desc'])
    if('detailed' in fileobj):
        print("-----------------------------------------------")
        print("Details:")
        print("-----------------------------------------------")
        for key,value in fileobj['detailed'].items():
            print(key + ": " + str(value))
    



