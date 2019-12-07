# https://leetcode.com/problems/course-schedule/
# this is a graph problem with adjacency lists 
from collections import defaultdict
# prerequisties is a list of sets of two integers
class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.graph = defaultdict(list)
        for edge in prerequisites:
            self.graph[edge[0]].append(edge[1])
            
    visited = set()

    # True if there is a cycle, False if not
    def visit(self, vertex):
      self.visited.add(vertex)
      for neighbour in self.graph[vertex]:
        if neighbour in self.visited or self.visit(neighbour):
          return True
      self.visited.remove(vertex)
      return False


    for i in range(numCourses):
        if visit(i):
            return False
        return True

