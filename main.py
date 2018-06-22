#!/usr/bin/env python3

# This file is part of the CTypes-Objects program Copyright (c) 2016 Jimmy
# Aguilar Mena.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (c) 2016 Jimmy Aguilar Mena.
# email: kratsbinovish@gmail.com
# date: 06/03/2016

import ctypes as C
import numpy as np

libarray = C.CDLL("./libarray.so")

libarray.create.restype = C.c_void_p
libarray.create.argtypes = [C.c_int, C.c_int, C.c_int]

libarray.printarray.restype = None
libarray.printarray.argtypes = [np.ctypeslib.ndpointer(C.c_void_p,
                                                       flags="C_CONTIGUOUS"),
                                C.c_int]

libarray.printclass.restype = None
libarray.printclass.argtypes = [C.c_void_p]

mylist = [0] * 5

for i in range(5):
    mylist[i] = libarray.create(3 * i, 3 * i + 1, 3 * i + 2)

arr = np.array(mylist, dtype=C.c_void_p)

libarray.printarray(arr, 5)

#--------------

# Declaro la funcion que recibe un puntero a la clase
# y le paso uno de los de la lista
libarray.printclass.restype = None
libarray.printclass(mylist[0])

# Creo una clase local clon de la de C
# con una funcion extra que no existe en C

class Myclass(C.Structure):
    _fields_ = [
        ("x", C.c_int),
        ("y", C.c_int),
        ("z", C.c_int)
        ]

    def myprint(self):
        print("From Python", self.x, self.y, self.z, sep=" ")

    def __del__(self):
        print("Deleting class", self.x, self.y, self.z, sep=" ")

libarray.create.restype = C.POINTER(Myclass)   # mejor asi desde el principio

# Creo una instancia de la clase local
testclass = Myclass(3, 2, 1)
testclass.myprint()                     # llamo la funcion local
libarray.printclass(C.byref(testclass)) # se la paso a C

#Creo una instancia de la clase local con el constructor de C
testclass2 = libarray.create(6, 5, 4)
testclass2.contents.myprint()           # llamo la funcion local
libarray.printclass(testclass2)         # se la paso a C

# casteo uno de los punteros de la lista como la clase local
# y llamo a la funcion que solo existe en la clase local

# Castea la clase como una de tipo local en el array
# Dejo esta opcion solo para mostrar el cast
casted = C.cast(mylist[0], C.POINTER(Myclass))[0]
casted.myprint()


