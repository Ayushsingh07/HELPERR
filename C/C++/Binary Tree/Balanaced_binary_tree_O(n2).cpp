//Balanced tree in binary tree

#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node *left;
    struct Node *right;

    Node(int val){
        data=val;
        left=NULL;
        right=NULL;
    }
};
//Assume empty tree has 0 height
int height(Node *root){
    if(root==NULL){
        return 0;
    }
    return max(height(root->left),height(root->right))+1;
}
bool isBalanced(Node *root){
    if(root==NULL){
        return true;
    }

    if(isBalanced(root->left)==false){
        return false;
    }
    if(isBalanced(root->right)==false){
        return false;
    }
    int lheight=height(root->left);
    int rheight=height(root->right);
    if(abs(lheight-rheight)<=1){
        return true;
    }
    else
    return false;
}

int main(){
    Node *root=new Node(1);
    root->left=new Node(2);
    root->right=new Node(3);
    root->left->left=new Node(4);
    root->left->right=new Node(5);
    root->right->left=new Node(6);
    root->right->right=new Node(7);
    if(isBalanced(root)){
        cout<<"Balanced Tree"<<"\n";
    }
    else{
        cout<<"Not Balanced Tree"<<"\n";
    }
    return 0;
}
/* 
         1
        / \
        2  3
       / \ / \
       4 5 6  7  
Output
Balanced Tree
Time complexity:O(n^2)
*/
