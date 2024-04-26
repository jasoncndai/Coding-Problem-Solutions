class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # create a graph where each edge away from city 0 has weight 1, edge towards it is 0
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        visited = [False] * n
        self.res = 0
        def dfs(node):
            # explore every connection from a node, adding weight to final response
            visited[node] = True
            for a, b in graph[node]:
                if not visited[a]:
                    self.res += b
                    dfs(a)
        dfs(0)
        return self.res
