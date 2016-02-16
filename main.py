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

#--------------

# Declaro la funcion que recibe un puntero a la clase
# y le paso uno de los de la lista

libarray.printclass.restype= None
libarray.printclass(mylist[0])

# Creo una clase local clon de la de C
# con una funcion extra que no existe en C

class Myclass(C.Structure):
    _fields_=[
            ("x",C.c_int),
            ("y",C.c_int),
            ("z",C.c_int)
            ]
    def myprint(self):
        print("From Python",self.x,self.y,self.z,sep=" ")

# Creo una instancia de la clase local y se la paso a C        
testclass = Myclass(3,2,1)

testclass.myprint() # llamo la funcion local
libarray.printclass(C.byref(testclass)) # se la paso a C

# casteo uno de los punteros de la lista como la clase local
# y llamo a la funcion que solo existe en la clase local

casted= C.cast(mylist[0],C.POINTER(Myclass))[0] #Castea la clase como una de tipo local
casted.myprint()

