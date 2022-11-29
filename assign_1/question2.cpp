#include<limits.h>
#include<float.h>
#include<iostream>
using namespace std;

int main(){
    cout<<"Memory size for int = "<<sizeof(int)<<"bytes"<<endl;
    cout<<"Memory size for float = "<<sizeof(float)<<"bytes"<<endl;
    cout<<"Memory size for bool = "<<sizeof(bool)<<"bytes"<<endl;
cout<<"Memory size for char = "<<sizeof(char)<<"bytes"<<endl;

cout<<"Minimum value of int = "<<INT_MIN<<" and Maximum value = "<<INT_MAX<<endl;
cout<<"Minimum value of float = "<<FLT_MIN<<" and Maximum value = "<<FLT_MAX<<endl;
cout<<"Minimum value of long = "<<LONG_MIN<<" and Maximum value = "<<LONG_MAX<<endl;

}