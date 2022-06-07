#!/usr/bin/python3

import os
if __name__ == "__main__":
    lista_direktorija = []
    for root,dirs,files in os.walk('a', topdown=True):
    #for dirs in os.walk('a', topdown=True):
        lista_direktorija += dirs
        lista_direktorija += files
        break;
        #print (root)
        #print (dirs)
       # print (files)
        #print ('--------------------------------')
    print(lista_direktorija)
