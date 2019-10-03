# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:39:25 2019

@author: Rahi
"""
#this code is to maintain file append data and read

def write(a):
    g=open("harrylog.txt","a+")
    def harry(n) :
    #this function will right line in harry file
        g.write(n)
    
    h=open("rohanlog.txt","a+")
    def rohan(j) :
    #this function will right line in rohan file
        h.write(j)
    
    l=open("bamko.txt","a+")
    def bamko(i) :
    #this function will right line in bamko file
        l.write(i)
    if a==1:
            b=input("type line to saave in harry'file")
            harry(b)
    elif a==2:
                c=input("type line to saave in rohan'file")
                rohan(c)
    elif a==3:
                    d=input("type line to saave in bamko'file")
                    bamko("\n",d)
    else:
                        print("rong input")
                        g.close()
                        h.close()
                        l.close()
def read(a):
    g=open("harrylog.txt")
    def harry(n):
    #this function will right line in harry file
        u=g.readline(n)
        print(u)
    
    h=open("rohanlog.txt")
    def rohan(j) :
    #this function will right line in rohan file
        e=h.readline(j)
        print(e)
    
    l=open("bamko.txt")
    def bamko(i) :
    #this function will right line in bamko file
        f=l.readline(i)
        print(f)
    if a==1:
            b=int(input("how many line you want to print"))
            (harry(b))
    elif a==2:
                c=int(input("how many line you want to print"))
                rohan(c)
    elif a==3:
                    d=int(input("how many line you want to print"))
                    bamko(d)
    else:
                        print("rong input")
                        g.close()
                        h.close()
                        l.close()
print("enter 1 for wright and 2 for read" )
y=int(input())
if y==1:
    print("press \n 1 for harry \n 2 for rohan \n 3 for bamko")
    a=int(input())
    write(a)
else:
    z=int(input("press \n 1 for harry \n 2 for rohan \n 3 for bamko"))
    read(z)