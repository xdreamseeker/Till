class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort();
        res = []
        self.dfs(candidates,target,0,[],res)
        return res

    def dfs(self,nums,target,index,path,res):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        else:
            for i in range(index,len(nums)):
                # path.append(nums[i])
                self.dfs(nums,target-nums[i],i,path+[nums[i]],res)


class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort();
        res = []
        self.dfs(candidates,target,0,[],res)
        return res

    def dfs(self,nums,target,index,path,res):
        if target < 0:
            return
        elif target == 0:
            if path not in res:
                res.append(path)
            return
        else:
            for i in range(index,len(nums)):
                # path.append(nums[i])
                self.dfs(nums,target-nums[i],i+1,path+[nums[i]],res)

if __name__=="__main__":
    app = Solution2()
    print(app.combinationSum([10, 1, 2, 7, 6, 1, 5],8))