class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates)<target:
            return None
        self.ans=[]
        ds=[]
        n=len(candidates)
        self.solve(0,candidates,target,ds,n)
        res=list(set(tuple(sorted(sub))for sub in self.ans))
        return res
    def solve(self,be,candidates,target,ds,en):
        if target==0:
            temp=ds[:]
            self.ans.append(temp)
            return
        if be==en:
            return
        for i in range(be,en):
            if candidates[i]<=target:
                ds.append(candidates[i])
                self.solve(i+1,candidates,target-candidates[i],ds,en)
                ds.pop()
        return


s = Solution()

print(s.combinationSum2([10,1,2,7,6,1,5], 8))
