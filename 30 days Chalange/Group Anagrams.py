class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            v=''.join(sorted(i))
            if v in dict:
                dict[v].append(i)
            else:
                dict[v]=[i]
        return list(dict.values())
