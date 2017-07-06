class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        if length <= 1:
            return length

        res = [1]*length

        # res[i] = max( res[j]) nums[i]
        for i in range(1,length):
            for j in range(0,i):
                if nums[i] > nums[j] and res[i] < res[j]+1: #res[i] < res[j]+1
                    res[i] = res[j]+1

        # print(res)
        return max(res)


if __name__=="__main__":
    # app = Solution()
    # print(app.lengthOfLIS([4,10,4,3,8,9]))

    strs=[]
    strs.append("asdfasdf0")
    strs.append("asdfasdf1")
    strs.append("asdfasdf2")
    # strs.append("asdfasdf")
    shortest = min(strs,key=len)
    print(shortest)

