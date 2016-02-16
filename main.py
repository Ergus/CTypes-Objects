#!/usr/bin/env python

import ctypes as C
import numpy as np

libarray = C.CDLL("./libarray.so")
                       
libarray.create.restype= C.c_void_p
libarray.create.argtypes=[C.c_int,C.c_int,C.c_int]

libarray.printarray.restype= None
libarray.printarray.argtypes=[np.ctypeslib.ndpointer(C.c_void_p, flags="C_CONTIGUOUS"),
                         C.c_int]

mylist = [0]*5

for i in range(5):
    mylist[i]=libarray.create(3*i,3*i+1,3*i+2)

arr=np.array(mylist, dtype=C.c_void_p)

libarray.printarray(arr,5)
