class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = set()
        currentPath = (0, 0)
        paths.add(currentPath)
        for p in path:
            print(currentPath)
            x, y = currentPath
            if p == "N":
                currentPath = (x,y+1)
            elif p == "S":
                currentPath = (x, y-1)
            elif p == "E":
                currentPath = (x+1, y)
            else:
                currentPath = (x-1, y)
            if currentPath in paths:
                return True
            else:
                paths.add(currentPath)
        print(paths)
        print(currentPath)
        return False