class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapp = {0 : -1}
        s, m = 0, 0
        for i in range(len(nums)):
            s += -1 if nums[i] == 0 else 1
            if s in mapp:
                m = max(m, i - mapp[s])
            else:
                mapp[s] = i
        return m
        
