class Solution:
    def maxProfit(self, p: List[int]) -> int:
        maxp=0
        for i in range(1,len(p)):
            if(p[i]>p[i-1]):
                maxp+=p[i]-p[i-1]
                
        return maxp
        
            
        
        
