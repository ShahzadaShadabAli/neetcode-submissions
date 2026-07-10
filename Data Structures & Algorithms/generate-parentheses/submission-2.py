class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(closedP, openP):
            if closedP == openP == n:
                res.append("".join(path))
                return

            if openP < n:
                path.append("(")
                dfs(closedP, openP+1)
                path.pop()

            if closedP < openP:
                path.append(")")
                dfs(closedP+1, openP)
                path.pop()

        dfs(0, 0)
        return res