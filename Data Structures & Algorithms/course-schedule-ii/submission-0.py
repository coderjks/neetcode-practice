from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort - khan's algo
        queue = deque()
        ans = []

        adjList = [[] for _ in range(numCourses)]
        inDegrees = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            inDegrees[a] += 1
            adjList[b].append(a)
        
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        

        while queue:
            i = queue.popleft()
            ans.append(i)
            numCourses -= 1
            for n in adjList[i]:
                inDegrees[n] -= 1
                if inDegrees[n] == 0:
                    queue.append(n)
                    
        return ans if numCourses == 0 else []