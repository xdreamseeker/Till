class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()
        if len(s) == 0:
            return 0
        # if s[-1] == " ":
        #     return 0
        word = s.split()
        # print(word[-1])
        return len(word[-1])


if __name__=="__main__":
    app = Solution()
    print(app.lengthOfLastWord("   "))