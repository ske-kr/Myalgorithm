## 잘못생각한점 : 모든 input data를 변환할 필요가 없이 sort시키면 동일한 anagram은 동일하게 출력된다
## 만약 sort할수 없다면 ? 그 때는 변환기를 사용할 필요가 있을까?

## 추가실수 - sorted사용시 list형태로 반환되기 때문에 다시 str화 시켜줘야하고
## 이때 str()이 아닌 "".join을 활용해야한다

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result=[]
        decode={}
        for i in strs:
            s="".join(sorted(i))
            if decode.get(s):
                decode[s].append(i)
            else:
                decode[s]=[]
                decode[s].append(i)
        
        keys=list(decode.keys())
        
        for key in keys:
            result.append(decode[key])
            
        return result