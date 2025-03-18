#include <bits/stdc++.h>

using namespace std;

// Function to implement Dijkstra's algorithm using an adjacency list
void dijkstra(int V, vector<vector<pair<int, int>>>& graph, int src) {
    // Create a priority queue to store (distance, vertex) pairs
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // Initialize distances to all vertices as infinite and distance to source as 0
    vector<int> distance(V, INT_MAX);
    distance[src] = 0;

    // Push the source node into the priority queue
    pq.push({0, src});

    while (!pq.empty()) {
        // Extract the vertex with the minimum distance
        int u = pq.top().second;
        pq.pop();

        // Traverse through all adjacent vertices of u
        for (const auto& neighbor : graph[u]) {
            int v = neighbor.first;   // neighbor vertex
            int weight = neighbor.second; // edge weight

            // If a shorter path to v is found
            if (distance[u] + weight < distance[v]) {
                distance[v] = distance[u] + weight;
                pq.push({distance[v], v}); // Push updated distance into the priority queue
            }
        }
    }
    // Print the shortest distances from the source vertex
    cout << "Vertex Distance from Source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << "\t\t" << distance[i] << endl;
    }
}

int main() {
    // Number of vertices in the graph
    int V, E;
    cout << "Enter number of vertices: ";
    cin >> V;

    cout << "Enter number of edges: ";
    cin >> E;

    // Create an adjacency list for the graph using vectors of pairs
    vector<vector<pair<int, int>>> graph(V);

    cout << "Enter edges in the format (u v weight):" << endl;
    for (int i = 0; i < E; ++i) {
        int u, v, weight;
        cin >> u >> v >> weight;

        // Add edges to the graph (undirected)
        graph[u].emplace_back(v, weight);
        graph[v].emplace_back(u, weight); // Comment this line if you want a directed graph
    }

    // Source vertex for Dijkstra's algorithm
    int src;
    cout << "Enter source vertex: ";
    cin >> src;

    // Call Dijkstra's algorithm with the specified source vertex
    dijkstra(V, graph, src);

    return 0;
}