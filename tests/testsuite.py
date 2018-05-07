#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
import subprocess
import sys

CRED    = '\33[31m'
CGREEN  = '\33[32m'
CWHITE  = '\33[37m'
CBLUE  = '\33[96m'
CPINK = '\33[95m'

def find_path():
    global path,way,path_shell
    path = os.getcwd() 
    if not is_inside(path,"test"):
        path_shell = path + "/"
        path += "/tests/"
    else:
        path_shell = path + "/../"
        path += "/"
    way = os.listdir(path)
    
def my_open():
    M = []
    for i in way:
        N = []
        if is_inside(i,"file"):
            for filename in os.listdir(path + i):
                N.append(exe ( path +  i + "/" , filename[0:len(filename)]))
            M.append(N)
    return M

def exe(my_cmd,filename):
    msh = path_shell + "./minishell"
    standart = "fail_standart"
    mine = "fail_minishell"
    cmd = msh + " "  + my_cmd + filename
    try:    
      mine = subprocess.Popen( cmd,  stdout=subprocess.PIPE,shell=True,stderr=subprocess.STDOUT)
      mine = mine.communicate()[0]
    except:
      pass
    try:
        standart = subprocess.Popen(my_cmd + "./" + filename, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        standart = standart.communicate()[0]
    except:
        pass   
    return [standart,mine,filename]



def is_inside(text,word):
    n = 0
    for i in text:
        if word[n] == i:
            n += 1
        else:
            n = 0
        if n == len(word):
            return True
    return False
def pretty(M):
    x = 0;
    for i in M:
        print '\n' + CPINK + way[x] + CWHITE + '\n'
        for j in i:
            print "[" + equal(j) + "] " + " " +  j[2] 
            if arg == "-print":
                print '\n' + CBLUE + "minishell output" + CWHITE + '\n'
                print [j[1]] 
                print '\n' + CBLUE + "Bash output" + CWHITE + '\n'
                print [j[0]] , '\n'               
        x += 1; 
    print ""
def equal(iput):
    
    if iput[0] == iput[1]:
        return CGREEN + "OK" + CWHITE
    else:
        return CRED + "KO" + CWHITE
    
def main():
    global arg
    arg = sys.argv[1:len(sys.argv)]
    if len(arg) > 0:
        arg = arg[0]
    find_path()
    result = my_open()
    pretty(result)
    
main()
