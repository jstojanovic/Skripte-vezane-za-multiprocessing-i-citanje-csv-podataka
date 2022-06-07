#!/usr/bin/env python
import multiprocessing
import subprocess
import os
import time

src = 'a'
lista_direktorija = []
def resink( dest ):
    subprocess.call(["rsync", "-arq", os.path.join(src, dest), 'backup/'])

def resink_parallel(lista_direktorija):
    with multiprocessing.Pool() as pool:
        pool.map(resink, lista_direktorija)#[[a/, backup/], b, ]

for root, dirs, files in os.walk(src, topdown=True):
    lista_direktorija += dirs
    lista_direktorija += files
    break;

print(lista_direktorija)
start_time = time.time()
resink_parallel(lista_direktorija)
duration = time.time() - start_time
print(f"duration: {duration} seconds")
