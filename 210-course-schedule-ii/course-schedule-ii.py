class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort. 

        # Build a map. 
        adj_mp = {}
        # Source -> [dest1, dest2, dest3]
        indegree = {}

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        for course, prereq in prerequisites:
            if course not in adj_mp:
                adj_mp[course] = []
            if prereq not in adj_mp:
                adj_mp[prereq] =[course]
            else:
                adj_mp[prereq].append(course)

        
            indegree[course] = indegree.get(course, 0) + 1
            if prereq not in indegree:
                indegree[prereq] = 0

        queue = []
        for course in range(numCourses):
            if course not in adj_mp:
                adj_mp[course] = []

        for course in range(numCourses):
            if indegree.get(course, 0) == 0:
                queue.append(course)
            
        top_order = []
        while len(queue) > 0:
            # Pop element from queue. 
            node = queue.pop(0)
            top_order.append(node)
            # reduce all the indegrees to which this nodes goes to zero. # All its neighbors. 
            for n in adj_mp[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        if numCourses == len(top_order):
            return top_order
        return []