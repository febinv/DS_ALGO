class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return None
        m=len(matrix)
        n=len(matrix[0])
        final=[]
        t,b,l,r=0,m-1,0,n-1
        dir=0
        while t<=b and l<=r:
            if dir==0:
                for i in range(l,r+1):
                    final.append(matrix[t][i])
                t+=1
                dir=1
            elif dir==1:
                for i in range(t,b+1):
                    final.append(matrix[i][r])
                r-=1
                dir=2
            elif dir==2:
                for i in range(r,l-1,-1):
                    final.append(matrix[b][i])
                b-=1
                dir=3
            elif dir==3:
                for i in range(b,t-1,-1):
                    final.append(matrix[i][l])
                l+=1
                dir=0
        return final



            
        
        