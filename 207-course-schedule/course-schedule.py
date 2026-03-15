class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sort. 

        # Build a map. 
        adj_mp = {}
        # Source -> [dest1, dest2, dest3]
        indegree = {}
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
        for n in indegree:
            if indegree[n] == 0:
                queue.append(n)
            
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
        
        return len(indegree) == len(top_order)
        