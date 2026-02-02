# Graph Data Structure
![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-yellow)

A clean, from-scratch implementation of the Graph data structure in Python, supporting both directed and undirected graphs with multiple representation methods.

## What is a Graph?

A **graph** is a non-linear data structure consisting of **vertices (nodes)** and **edges** that connect pairs of vertices. Graphs are used to model relationships and connections between objects.

**Components:**
- **Vertex (Node)**: A fundamental unit representing an entity
- **Edge**: A connection between two vertices
- **Weight**: Optional value associated with an edge (for weighted graphs)

**Types:**
- **Directed Graph (Digraph)**: Edges have direction (A → B ≠ B → A)
- **Undirected Graph**: Edges are bidirectional (A - B means both A → B and B → A)
- **Weighted Graph**: Edges have associated weights/costs
- **Unweighted Graph**: All edges are equal

## Graph Representations

### 1. Adjacency Matrix
A 2D array where `matrix[i][j] = 1` indicates an edge from vertex i to vertex j.

**Pros:** O(1) edge lookup  
**Cons:** O(V²) space, inefficient for sparse graphs

```python
# Example: 3 vertices (0, 1, 2)
# Edges: 0→1, 1→2, 2→0
matrix = [
    [0, 1, 0],  # vertex 0
    [0, 0, 1],  # vertex 1
    [1, 0, 0]   # vertex 2
]
```

### 2. Adjacency List
A dictionary/list where each vertex maps to a list of its neighbors.

**Pros:** O(V + E) space, efficient for sparse graphs  
**Cons:** O(V) edge lookup in worst case

```python
# Same graph as above
adj_list = {
    0: [1],
    1: [2],
    2: [0]
}
```

### 3. Edge List
A list of all edges as tuples (from, to, weight).

**Pros:** Simple, space-efficient  
**Cons:** Slow neighbor lookups

```python
edges = [(0, 1), (1, 2), (2, 0)]
```

## Implementation Details

This implementation uses an **adjacency list** representation for optimal space and time complexity in sparse graphs.

### Core Methods

**Graph Construction:**
```python
graph = Graph()                    # Create empty graph
graph = Graph(directed=True)       # Create directed graph
```

**Adding Vertices:**
```python
graph.add_vertex(0)                # Add vertex with id 0
graph.add_vertex('A')              # Vertices can be any hashable type
```

**Adding Edges:**
```python
graph.add_edge(0, 1)               # Unweighted edge
graph.add_edge(0, 1, weight=5)     # Weighted edge
```

**Querying:**
```python
graph.get_neighbors(0)             # Returns list of adjacent vertices
graph.has_edge(0, 1)               # Check if edge exists
graph.get_weight(0, 1)             # Get edge weight
len(graph)                         # Number of vertices
```

**Traversal:**
```python
graph.bfs(start_vertex)            # Breadth-First Search
graph.dfs(start_vertex)            # Depth-First Search
```

### Time Complexity

| Operation | Adjacency List | Adjacency Matrix |
|-----------|----------------|------------------|
| Add Vertex | O(1) | O(V²) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V + E) | O(V²) |
| Remove Edge | O(E) | O(1) |
| Check Edge | O(V) | O(1) |
| Get Neighbors | O(1) | O(V) |
| BFS/DFS | O(V + E) | O(V²) |

### Space Complexity
- **Adjacency List**: O(V + E)
- **Adjacency Matrix**: O(V²)

## Common Graph Algorithms

Graphs are fundamental to many algorithms:

- **Shortest Path**: Dijkstra's, Bellman-Ford, A*
- **Minimum Spanning Tree**: Kruskal's, Prim's
- **Traversal**: BFS, DFS
- **Cycle Detection**: DFS-based, Union-Find
- **Topological Sort**: DFS, Kahn's algorithm
- **Connectivity**: Tarjan's, Kosaraju's

## Usage Example

```python
from Graph import Graph

# Create an undirected graph
graph = Graph(directed=False)

# Add vertices
for vertex in ['A', 'B', 'C', 'D']:
    graph.add_vertex(vertex)

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

# Query the graph
print(graph.get_neighbors('A'))     # ['B', 'C']
print(graph.has_edge('A', 'B'))     # True
print(len(graph))                   # 4 vertices

# Traverse the graph
bfs_order = graph.bfs('A')          # ['A', 'B', 'C', 'D']
```

**Author:** Nikhil Singla  
**GitHub:** [github.com/Nikhil-Singla](https://github.com/Nikhil-Singla/)  
**LinkedIn:** [linkedin.com/in/nsingla](https://www.linkedin.com/in/nsingla)

*Part of The Recreational Center - Building software fundamentals from first principles*
