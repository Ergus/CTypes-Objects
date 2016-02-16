
#include "libarray.h"

myclass::myclass(int ox,int oy, int oz):
  x(ox),y(oy),z(oz){
  
  }


myclass* create(int ox,int oy, int oz){
  myclass* ptr=new myclass(ox,oy,oz);
  return ptr;
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
