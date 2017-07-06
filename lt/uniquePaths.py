class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res =  [([1] * (n+1)) for i in range(m+1)]
        for i in range(2,m+1):
            for j in range(2,n+1):
                res[i][j] = res[i][j-1] + res[i-1][j]

        return res[m][n]


if __name__=="__main__":
    app = Solution()
    app.uniquePaths(2,2)
    print(app.uniquePaths(2,2))
    