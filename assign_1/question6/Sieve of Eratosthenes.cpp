#include<iostream>
using namespace std;

void primeviaSOE(int n){
    int arr[n+1]={0};//made an array upto that number index and filled with 0 to indicate its not covered


for(int i=2;i<=n;i++){
    if(arr[i]==0){
        for(int j=i*i;j<=n;j=j+i){
            arr[j]=1;//marked with 1 to show that its not a prime i.e mmultiple of previous no.
        }

    }
}
for(int i=2;i<=n;i++){
if(arr[i]==0){
    cout<<i<<",";// printing all the unmarked i
}
}
}
int main(){
    int n;
    cout<<"enter the number = ";
    cin>>n;
    primeviaSOE(n);
return 0;
}