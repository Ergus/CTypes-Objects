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

#ifndef libarray_h
#define libarray_h

#include <iostream>

using namespace std;

extern "C"{

class myclass{
    public:
        myclass(int,int,int);
        void print(){
            cout<<"x="<<x<<" y="<<y<<" z="<<z<<endl;
            };

    private:
        int x,y,z;
    };

myclass* create(int,int,int);

void printarray(myclass**, int);

void printclass(myclass*);
    
    
}

#endif
