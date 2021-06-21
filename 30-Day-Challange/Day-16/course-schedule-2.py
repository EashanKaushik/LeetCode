from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):

        adj_matrix = defaultdict(list)
        visited, cycle = set(), set()
        path = list()

        for prereq in prerequisites:
            adj_matrix[prereq[0]].append(prereq[1])

        def dfs(course):

            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for prereq in adj_matrix[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            path.append(course)
            return True

        for course in range(0, numCourses):
            if not dfs(course):
                return []

        return path



s = Solution()
print(s.findOrder(2, [[1, 0], [0, 1]]))
