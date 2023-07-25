#include<iostream>
#include<unordered_map>
using namespace std;

int main(){
    int y;
    cin>>y;
    int arr[y];

    for(int i;i<y;i++){
        cin>>arr[i];
    
    }

//pre processing

unordered_map<int,int>m;
for(int i;i<y;i++){

    m[arr[i]]++;
}

    int n,x;
    cin>>n;

    for(int i; i<n;i++){
        cin>>x;
        cout<<m[x];
    }

    return 0;
}

