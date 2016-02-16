#include "libarray.h"

int main(){
    myclass **myarray=new myclass*[5];

    for(int i=0;i<5;i++){
        myarray[i]=create(3*i,3*i+1,3*i+2);
        }
    
    printarray(myarray,5);

    for(int i=0;i<5;i++){
        delete myarray[i];
        }
    delete [] myarray;
    
    return 0;
    }
