#!/bin/usr/python3

import sys, os
x =0 
count = 0
mylist=[]
i=""
with open(sys.argv[1], "rb") as f:
    while f.read(1):
        o = f.seek(-1,1)
        w = f.read(1)
        n = w.decode("utf-8")
        x = ord(n)

        if x>=33 and x <= 126:
            mylist.append(n)
        else:
            mylist.append(".")

        g = w.hex()

        print("0x"+g,end=" ")
        count +=1
        if count == 16:

            print("|",*mylist,sep="")
            mylist=[]
            print("\n")
            count=0
            print("{:10s}".format(hex(o)),end="   |")
