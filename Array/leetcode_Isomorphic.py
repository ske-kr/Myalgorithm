## 간단한 dic활용문제
## 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicA={}
        dicB={}
        
        for i in range(len(s)):
            if dicA.get(s[i]):
                if dicA[s[i]]!=t[i]:
                    return False
            else:
                dicA[s[i]]=t[i]
            
            if dicB.get(t[i]):
                if dicB[t[i]]!=s[i]:
                    return False
            else:
                dicB[t[i]]=s[i]
                
        
        return True