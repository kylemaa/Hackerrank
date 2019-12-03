# https://leetcode.com/problems/queue-reconstruction-by-height/description/
class Solution:
    def reconstruct(self, people):
        res = []
        people.sort(key = lambda x: (-x[0], x[1])) 
        print(people)
        for p in people: 
            res.insert(p[1], p)
            print(p[1],p)
        
        print(res)



people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstruct(people))