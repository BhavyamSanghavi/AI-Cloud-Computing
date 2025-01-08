#include<bits/stdc++.h>
using namespace std;

void bfsRecursive(int n, vector<vector<int>>& edgelist, queue<int>& q, unordered_set<int>& visited) {
    visited.insert(n);
    cout << n << " ";

    for (int neighbor : edgelist[n]) {
        if (visited.find(neighbor) == visited.end()) {
            q.push(neighbor);
            visited.insert(neighbor);
        }
    }

    if (!q.empty()) {
        int next_node = q.front();
        q.pop();
        bfsRecursive(next_node, edgelist, q, visited);
    }
}

void dfsRec(vector<vector<int>> &adj, vector<bool> &visited, int s){
    visited[s] = true;
    cout << s << " ";

    for (int i : adj[s])
        if (visited[i] == false)
            dfsRec(adj, visited, i);
}


int main() {
    // Define number of nodes
    int nodes;
    cout<<"Enter number of nodes:";     cin>>nodes;

    // Example: Edge list representation of an undirected graph
    vector<vector<int>> edgelist(nodes);
    for(int i=0;i<nodes;i++)
    {
        int data=0;
        do{
            cout<<"Enter nodes connected with "<<i<<":";
            cin>>data;
            if(data!=-1)
                edgelist[i].push_back(data);
        }while(data!=-1);
    }

    // Initialize a queue for BFS and a set for tracking visited nodes
    queue<int> q;
    unordered_set<int> visited;

    cout << "BFS Traversal: ";
    bfsRecursive(0, edgelist, q, visited);
    cout << endl;

    vector<bool> visit(nodes,0);
    cout<<"DFS Tracersal: ";
    dfsRec(edgelist,visit,0);
    cout<<endl;
    return 0;
}
