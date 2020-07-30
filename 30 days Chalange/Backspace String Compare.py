class Solution:
   #def backspaceCompare(self, S: str, T: str) -> bool:
    def backspaceCompare(self, S, T):
        a=''
        b=''
        for i in S:
            if i!='#':
                a=a+i
            else:
                a=a[:-1]
        for i in T:
            if i!='#':
                b+=i
            else:
                b=b[:-1]
        return a==b
                
        
