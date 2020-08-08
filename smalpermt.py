class Solution(object):
    def prevPermOpt1(self, A): 
        n = len(A)
        if n<=1: return A
        l = n-2
        while l>=0 and A[l]<=A[l+1]:
            l -= 1
        if l < 0: 
            return A
        r = n-1
        while A[r]>=A[l]:
            r -= 1
        while A[r]==A[r-1]:
            r -= 1
        A[l],A[r] = A[r],A[l]
        return A
val=Solution()
n=list(map(int,input().split()))
print(*val.prevPermOpt1(n))
