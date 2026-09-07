from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort - khan's algo
        queue = deque()

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
            numCourses -= 1
            for n in adjList[i]:
                inDegrees[n] -= 1
                if inDegrees[n] == 0:
                    queue.append(n)
        return numCourses == 0



