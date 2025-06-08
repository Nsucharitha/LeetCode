class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        ans = []
        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            states[node] = visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node] = visited
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
        