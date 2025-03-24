# include <iostream>
# include <string>
# include <vector>
using namespace std;

//return the length of the longest common subsequence

int LCS(string& s1,string& s2,int n,int m)
{
   // if eny one of the string reach length 0 , than the algorithm will be finish.
   if(n==0 || m==0){
     return 0;
   }
   
   // The letter will be same , we add that letter
   if(s1[n-1]==s2[m-1]){
   
       return 1+LCS(s1,s2,n-1,m-1);
   }
   
   /* The letters will be not same , we call the two sub recursive calls and 
   take the maximum length of the common subsequnce */
   else{
      return max(LCS(s1,s2,n-1,m),LCS(s1,s2,n,m-1));
   }
   return 0;
}

int LCS_optimal(string& s1,string& s2,int n,int m,vector<vector <int>>& mat)
{
   // if eny one of the string reach length 0 , than the algorithm will be finish.
   if(n==0 || m==0){
     return 0;
   }
   
   if(mat[n][m]!=-1){
   
       return mat[n][m];
   }
   // The letter will be same , we add that letter
   if(s1[n-1]==s2[m-1]){
   
       return mat[n][m]=1+LCS_optimal(s1,s2,n-1,m-1,mat);
   }
   
   /* The letters will be not same , we call the two sub recursive calls and 
   take the maximum length of the common subsequnce */
   else{
      return mat[n][m]=max(LCS_optimal(s1,s2,n-1,m,mat),LCS_optimal(s1,s2,n,m-1,mat));
   }
   return 0;
}

int  main(){

   string s1,s2;
   
   cout<<"Enter the String 1:";
   cin>>s1;

   cout<<"Enter the String 2:";
   cin>>s2;
    int n = s1.length();
    int m = s2.length();
    vector<vector<int>> mat(n+1,vector<int>(m+1,-1));
    
   cout<<"The lenght of the LCS is: "<<LCS_optimal(s1,s2,n,m,mat)<<endl;
   return 0;
}
