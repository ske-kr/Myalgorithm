
#default dict 구조
#상당히 유용한 구조로 다른 문제에서 dictionary를 사용했던 문제는 대부분 호환가능하며
# 오히려 더 좋은 성능을보이게 할 수 있다.
#예를 들어 s=asdf일때 알파벳 갯수를 센다고 가정하자
# 처음에 a의 갯수를 샐때 dic을 선언하고 사용한다면
# key값 a가 존재하는지를 체크하고 없으면 initialization을 해야한다
# 그러나 defaultdic[int]로 선언했다면 dic=defaultdict[int]으로 선언후
# 바로 dic[a]로 접근하면 이미 0으로 초기화 되어있기 떄문에 바로 사용가능하다.

from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def ifSubseq(word):
            prev_i = -1
            for i,v in enumerate(word):
                if not dict_s[v]:
                    return 0
                for cur_i in dict_s[v]:
                    if prev_i<cur_i and i<=cur_i:
                        prev_i = cur_i
                        break
                    if cur_i == dict_s[v][-1]:
                        return 0
            return 1
        
        count = 0
        dict_s = defaultdict(list)
        for i,v in enumerate(S):
            dict_s[v].append(i)
        for word in words:
            count += ifSubseq(word)
        return count