 TreeNode* bst (vector<int>& nums , int start , int end )
    {
        
        if(start > end)
            return nullptr;
        int mid = (start+end)/2;
        TreeNode* root= new TreeNode(nums[mid]);
        root->left=bst(nums,start,mid-1);
        root->right=bst(nums,mid+1,end);
        
        return root;
        
        
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int n=nums.size()-1;
        return bst(nums,0,n);
        
        
    }
