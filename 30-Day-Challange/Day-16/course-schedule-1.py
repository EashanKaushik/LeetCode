from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        adj_matrix = {num:[] for num in range(0, numCourses)}

        for prereq in prerequisites:
            adj_matrix[prereq[0]].append(prereq[1])

        cycle = set()

        def dfs(course):

            if course in cycle:
                return False


            if len(adj_matrix[course]) > 0:
                cycle.add(course)

                for prereq in adj_matrix[course]:
                    if not dfs(prereq):
                        return False
                    else:
                        adj_matrix[course].remove(prereq)

                cycle.remove(course)

            return True

        for course in range(0, numCourses):
            if not dfs(course):
                return False
        return True
        


s = Solution()
print(s.canFinish(2, [[1, 0], [0, 1]]))
