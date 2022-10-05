 vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        // Code here
        queue<int>q;
       int vis[V]={0};
        vis[0]=1;
        q.push(0);
        vector<int>bfs;
        while(!q.empty()){
            int node=q.front();
            q.pop();
            bfs.push_back(node);
            for(auto it:adj[node]){
                if(!vis[it]){
                    vis[it]=1;
                    q.push(it);
                }
            }
        }
        return bfs;
    }

// Expected Time Complexity: O(V + E)
// Expected Auxiliary Space: O(V)
