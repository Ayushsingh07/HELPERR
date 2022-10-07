#include<bits/stdc++.h>
using namespace std;

vector<int> topo(int N, vector<int> adj[]) {

	queue<int> q; 
	vector<int> indegree(N, 0); 

	// topo is answer vector
	vector<int> topo;

	for(int i = 0;i<N;i++) {
		for(auto it: adj[i]) {
			indegree[it]++; 
		}
	}
	
	// push all the nodes with indegree 0 into queue
	for(int i = 0;i<N;i++) {
		if(indegree[i] == 0) {
			q.push(i); 
		}
	}

	while(!q.empty()) {
		int node = q.front(); 
		q.pop(); 
		// no more dependency for this node so push into into our answer
		topo.push_back(node);

		for(auto it : adj[node]) {
			indegree[it]--;

			// if indeg == 0 push into queue 
			if(indegree[it] == 0) {
				q.push(it); 
			}
		}
	}
	return topo;
}


int main()
{
	int n=6;
	vector<int> adj[n];
	adj[5].push_back(2);
	adj[5].push_back(0);
	adj[4].push_back(0);
	adj[4].push_back(1);
	adj[3].push_back(1);
	adj[2].push_back(3);

	vector<int> order=topo(n, adj);
	cout<<"Topological order is : ";
	for(auto it:order){
		cout<<it<<" ";
	}
    
    return 0;
}
