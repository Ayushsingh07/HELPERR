class Solution {
    
    
  private:
    void dfs(int node,vector<int> adj[],vector<int>&ans,int vis[]){
        vis[node]=1;
        ans.push_back(node);
        for(auto it:adj[node]){
            if(vis[it]!=1){
                dfs(it,adj,ans,vis);
            }
        }
    }
  public:
    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
        // Code here
        int vis[V]={0};
        int start=0;
        vector<int>ans;
        dfs(start,adj,ans,vis);
        return ans;
    }
};

/*
TC- O(V+2E)
SC-O(V)
*/
