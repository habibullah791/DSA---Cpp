#include <iostream>
using namespace std;

int funct(int key){
    cout<<key;

    if (key < 14){
        funct(funct(funct(++key)));
    }
    return key;
}

int main(){
    cout<<funct(12);
    return 0;
}