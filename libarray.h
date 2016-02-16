
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
}

#endif
