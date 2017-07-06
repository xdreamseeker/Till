class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res=[]
        for i in range(1,len(nums)+1):
            self.dfs(nums,i,[],res)

        res.append([])
        return res

    def dfs(self,nums,k,path,res):
        if k == 0:
            res.append(path)
        for  i in range(0,len(nums)):
            newnums = nums[i+1:]
            self.dfs(newnums,k-1,path+[nums[i]],res)

if __name__=="__main__":
    app=Solution()
    print(app.subsets([1,2,3]))