int height(TreeNode* root)
    {
        if(root==nullptr)
            return 0;
        return 1+max(height(root->left),height(root->right));
    }
    void getsum(int &sum, TreeNode* root, int cht, int ht)
    {
        if(root==nullptr)
            return;
        if(ht==cht)
        {
            sum+=root->val;
            return;
        }
        getsum(sum, root->left, cht+1,ht);
        getsum(sum, root->right, cht+1,ht);
    }
    int deepestLeavesSum(TreeNode* root) {
        int ht=height(root);
        int sum=0;
        getsum(sum,root,1,ht);
        return sum;
        
    }
