class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False]*n
        res = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if not visited[node]:
                visited[node] = True
                for nei in adj[node]:
                    dfs(nei)

        for node in range(n):
            if not visited[node]:
                dfs(node)
                res+=1
        return res
