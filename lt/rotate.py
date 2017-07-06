class Solution(object):
    def rotate(self, matrix):
        # self.printM(matrix)
        line = int(len(matrix)/2)
        step = len(matrix)-1
        n = len(matrix) -1

        for i in range(0,line):
            for j in range(i,len(matrix)-i-1):
                print("%d,%d"%(i,j))
                # matrix[i][j] matrix[i+step][j]  matrix[i+step][j+step] matrix[i][j+step]
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] =matrix[j][n-i]
                matrix[j][n-i] = temp

        # self.printM(matrix)

    def printM(self,matrix):
        for i in range(len(matrix)):
            print(matrix[i])



if __name__=="__main__":
    app = Solution()
    matrix=[]
    matrix.append([1,2,3,4])
    matrix.append([2,2,3,4])
    matrix.append([3,2,3,4])
    matrix.append([5,2,3,4])
    app.rotate(matrix)