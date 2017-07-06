class Solution():
    def longestSubStr(self,s1,s2):
        """

        :param s1:
        :param s2:
        :return:

        x[0-n]
        y[0-m]
        Z[0-k]

        c[i,j] = c[i-1,j-1]+1  when xi==yj
               = 0 when xi!=yj
        """
        if len(s1)==0 or len(s2)==0:
            return 0
        c = [[0 for j in range(len(s2))] for i in range(len(s1))]
        z = []
        for i in range(0,len(s1)):
            for j in range(0,len(s2)):
                if s1[i] == s2[j]:
                        c[i][j] = c[i-1][j-1] + 1   #此处利用了c[-1][-1] == 0的特性，其他语言不可以这样
                else:
                    c[i][j] = 0

        print(c)
        return c[len(s1)-1][len(s2)-1]



if __name__=="__main__":
    app = Solution()
    print(app.longestSubStr("23ww","1234523"))