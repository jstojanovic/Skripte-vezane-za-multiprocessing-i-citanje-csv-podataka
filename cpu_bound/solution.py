#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
from os import walk 


src= "a/"
dest="backup/"

def backupData(dir):
    print("dir = "+ src+dir +" dest = " + dest+dir)
    subprocess.call(["rsync", "-arq", src+dir, dest+dir]) 


dirList = []

for (root, dirs, files) in walk(src):
    dirList.extend(dirs)
    break;

print (dirList)

#p= Pool(len(dirList))

#p.map(backupData, dirList)
