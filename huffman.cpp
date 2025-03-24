#include <iostream>
#include <bits/stdc++.h> 
using namespace std;

struct node
{
    char data;
    unsigned frq;

    node * left,*right;

    node(char data,unsigned feq){

        this->data=data;
        this->frq=feq;
        this->left=nullptr;
        this->right=nullptr;
    }

};

struct compare
{
    bool operator()(node * left,node * right){
        return (left->frq > right->frq);
    }
};

void code(node* root,string c){

        if(!root){

             return ;

        }

        if(root->data!='$'){

            cout<< root->data <<" : "<<c<<endl;

        }

        code(root->left,c+"0");
        code(root->right,c+"1");



}

void huffmanCode(char arr[],int freq[],int size){

      priority_queue <node*,vector<node*>,compare> que;
      node* l,*r,*t;

      for(int i=0;i<size;i++){

           que.push(new node(arr[i],freq[i]));

      }

     while(que.size()>1){

         l=que.top();
         que.pop();
         r=que.top();
         que.pop();

        t=new node('$',l->frq+r->frq);
        t->left=l;
        t->right=r;
        que.push(t);

     }

     code(que.top(),"");


}


int main(){

    char arr[] = { 'a', 'b', 'c', 'd', 'e', 'f' }; 
    int freq[] = { 5, 9, 12, 13, 16, 45 }; 

    int size=sizeof(arr)/sizeof(arr[0]);

    huffmanCode(arr,freq,size);

    return 0;


}