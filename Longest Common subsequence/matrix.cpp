# include <iostream>
# include <string>
# include <vector>
using namespace std;

int matrix(string & s1, string & s2 , int n, int m, vector<vector<int>> mat){

         for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
               if(s1[i]==s2[j]){
               
                   mat[i][j]=mat[i-1][j-1];
               }
               else{
                  mat[i][j]=max(mat[i-1][j],mat[i][j-1]);
               }
            }
         
         }
         return mat[n][m];
}


int  main(){

   string s1,s2;
   
   cout<<"Enter the String 1:";
   cin>>s1;

   cout<<"Enter the String 2:";
   cin>>s2;
    int n = s1.length();
    int m = s2.length();
    vector<vector<int>> mat(n+1,vector<int>(m+1,0));
    
   cout<<"The lenght of the LCS is: "<<matrix(s1,s2,n,m,mat)<<endl;
   return 0;
}
