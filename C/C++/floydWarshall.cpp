
class Solution {
  public:
	void shortest_distance(vector<vector<int>>&matrix){
	    // Code here
	    //at any point k, matrix[i][j] stores min cost to reach from i to j via k intermediate nodes
    int v=matrix.size();
    for(int k=0;k<v;k++){ //vertex as intermediate 
        for(int i=0;i<v;i++){ //all vertex as source one by one
          for(int j=0;j<v;j++){ //destination 
            if(matrix[i][k]==-1 || matrix[k][j]==-1){
                continue;
            }
            int cur=matrix[i][k]+matrix[k][j];
            
            if(matrix[i][j]==-1){
                matrix[i][j]=cur;
            }
            
            else matrix[i][j]=min(matrix[i][j],cur);
          }
        }
    }
	}
};
