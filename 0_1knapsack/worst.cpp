# include<iostream>
# include<vector>
using namespace std;

int knapsack(int w,vector<pair<int, int>> s,int n){

     if(n==0 || w==0){
        return 0;
     }

     if(s[n-1].first>w){
       
       return knapsack(w,s,n-1);
       
     }
     else{
     
        return max(knapsack(w,s,n-1),s[n-1].second+knapsack(w-s[n-1].first,s,n-1));
     
     }
     return 0;

}    



int main(){

    vector<pair<int ,int>> s={{2,10},{3,20},{4,50},{5,60}};
    cout<<knapsack(8,s,4)<<endl;

}
