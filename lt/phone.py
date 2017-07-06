class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        pos = -1
        for i in range(0,len(nums)):
            if target > nums[i]:
                continue
            elif target == nums[i]:
                return i
            else:
                pos=i
                break

        return pos


if __name__=="__main__":
    app = Solution()
    print(app.searchInsert([2,3,5,6],2))