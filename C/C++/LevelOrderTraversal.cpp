vector<vector<int>> levelOrder(TreeNode* root) {
        
        vector<vector<int>>ans;
        if(root==nullptr)
            return ans;
        queue<TreeNode*>q;
        q.push(root);
        
        while(!q.empty())
        {
            int sz=q.size();
            vector<int>lev;
            for(int i=0;i<sz;i++)
            {
                TreeNode* node=q.front();
                q.pop();
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
                lev.push_back(node->val);
            }
            ans.push_back(lev);
        }
        return ans;
        
    }
}
