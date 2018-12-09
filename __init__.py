#!/usr/bin/python3
import py_compile as pyc
import os
import fnmatch

listOfFiles = os.listdir('.')
pattern = "*.py"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            pyc.compile(entry)
