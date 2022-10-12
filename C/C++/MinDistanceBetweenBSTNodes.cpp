 vector<int>v;
    void inorder(TreeNode* root)
    {
        if(root==nullptr)
            return;
        inorder(root->left);
        v.push_back(root->val);
        inorder(root->right);
    }
   int minDiffInBST(TreeNode* root) {
        
        if(root==nullptr)
            return 0;
        inorder(root);
        int mi=INT_MAX;
        for(int i=0;i<v.size()-1;i++)
        {
            mi=min(abs(v[i]-v[i+1]),mi);
        }
        return mi;
    }
