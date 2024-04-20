class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Graph problem, explore edges of nodes in graph by DFS or BFS
        # Use visited array of length n to track if node has been visited
        provinces = 0
        n = len(isConnected)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                self.dfs(isConnected, visited, i)
                provinces += 1
        return provinces
    
    # DFS Approach
    def dfs(self, isConnected, visited, i):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(isConnected, visited, j)
        return
        
    # BFS Approach
    def bfs(self, isConnected, visited, i):
        visited[i] = True
        queue = [i]
        while queue:
            i = queue.pop()
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    queue.append(j)
        return