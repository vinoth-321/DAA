# include<iostream>
# include<vector>
using namespace std;

int knapsack(int w,vector<pair<int, int>> s,int n,int &arr[][]){

     if(n==0 || w==0){
        return 0;
     }
     
     if(arr[n][w]!=-1){
        return arr[n][w];
     }

     if(s[n-1].first>w){
       
       arr[n][w] =knapsack(w,s,n-1,arr);
       return arr[][];
     }
     else{
     
        arr[n][w]= max(knapsack(w,s,n-1,arr),s[n-1].second+knapsack(w-s[n-1].first,s,n-1,arr));
        return arr[n][w];
     }
     return 0;

}    



int main(){

    vector<pair<int ,int>> s={{2,10},{3,20},{4,50},{5,60}};
    int arr[4][8];
    cout<<knapsack(8,s,4,arr)<<endl;

}
