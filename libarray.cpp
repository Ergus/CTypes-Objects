/*
 * This file is part of the CTypes-Objects program Copyright (c) 2015 Jimmy
 * Aguilar Mena.
 *
 * This program is free software: you can redistribute it and/or modify  
 * it under the terms of the GNU General Public License as published by  
 * the Free Software Foundation, version 3.
 *
 * This program is distributed in the hope that it will be useful, but 
 * WITHOUT ANY WARRANTY; without even the implied warranty of 
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License 
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "libarray.h"

myclass::myclass(int ox,int oy, int oz):
  x(ox),y(oy),z(oz){
  
  }


myclass* create(int ox,int oy, int oz){
  return new myclass(ox,oy,oz);
  }

void printarray(myclass** array, int size){
    for(int i=0;i<size;i++){
        array[i]->print();
        }    

    }

void printclass(myclass* a){
    cout<<"From C ";
    a->print();
    }
