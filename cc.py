#!/usr/bin/python3
import os
import sys

def createDir(path):
    if (os.path.exists(path)):
        print("Directory already exists")
    else:
        os.mkdir(path)
        print("Succes")

def createMakeFile(path):
    os.chdir(path)
    path = '/home/artem/.vim/templates/makefile.txt'
    if (os.path.exists(path)):
        with open(path, 'r') as rf:
            with open('makefile', 'w') as wf:
                for line in rf:
                    wf.write(line)
    else:
        print("error")

print("Enter contest name :")

contest_name = input()
par_dir = "/home/artem/vimcp/"
path = os.path.join(par_dir, contest_name)
createDir(path)
createMakeFile(path)


