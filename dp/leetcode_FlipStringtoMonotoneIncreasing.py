## ones => 1로 뒤집어야하는 0의수
## zeros => 0으로 뒤집어야하는 1의수
## 앞에서부터 체크하는데 0이면 1로 뒤집어야하고 zeros가 0이라면 안뒤집어도 된다는말이므로 0으로다시 갱신
## 1이나온다면 zeros가 1로 바뀌고, ones와의 비교를 통해 갱신

## 단순 구현이라고 쉽게 생각하지말고 
## 논리적으로 전개시켜보는 연습

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros=0
        ones=0
        
        for i in s:
            if i=='1':
                zeros+=1
            else:
                ones+=1
            ones=min(zeros,ones)
        return ones