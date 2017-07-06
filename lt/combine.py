class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i for i in range(1,n+1)]

        if k > n:
            k=n
        self.dfs(nums,[],k,res)
        return res

    def dfs(self,nums,path,k,res):
        if k == 0:
            res.append(path)

        for i in range(0,len(nums)):
            newnums = nums[i+1:]
            self.dfs(newnums,path+[nums[i]],k-1,res)
    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i for i in range(1,n+1)]



if __name__=="__main__":
    app = Solution()
    print(app.combine(20,16))
