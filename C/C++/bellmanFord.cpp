public:
	int isNegativeWeightCycle(int n, vector<vector<int>>edges){
	    int src = 0;
	    int inf = 1e8;
	    vector<int> dist(n, inf);
	    dist[src] = 0;
	    for(int i=1; i<n; i++){
	        for(auto it: edges){
	            if(dist[it[0]] + it[2] < dist[it[1]]){
	                dist[it[1]] = dist[it[0]] + it[2];
	            }
	        }
	        
	    }
	    
	    for(auto it: edges) {
        if(dist[it[0]] + it[2] < dist[it[1]]) {
            return true;
             
        }
    }
    
    return false;
	}
};
