void funcpost(Node* root)
    {
        if(root==nullptr)
            return;
        for(auto child:root->children )
        {
            funcpost(child);
        }
        v.push_back(root->val);
        
    }
    vector<int> postorder(Node* root) {
        if(root==nullptr)
            return v;
        funcpost(root);
        return v;
        
        
        
    }
