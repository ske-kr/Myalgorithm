#leetcode find shortest superstring문제
# sequencing과도 연관있는문제다
# 아래부분은 내가구현한부분인데 greedy하게 구현해서 틀린답이다
# i,j가 겹치는값을 일일히 다 조사한 뒤에
# dp를 이용해서 어떤순서로 delete해야 최종 겹치는부분이 가장 많은지를 알수있음
#ㅠㅠ..

class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1<<N)]
        parent = [[None] * N for _ in xrange(1<<N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(xrange(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)

##여긴 나의 잘못된 코드이다.
## greedy하게 구현했으므로
## 최적선택만 해나갔기 때문에 안되는예시가 생긴다
## ex)["abcdef","efde","defab"]
def overlap(a,b):
    if len(a)>=len(b):
        long=a
        short=b
    else:
        long=b
        short=a
    if short in long:
        return [len(short),long]
    for i in range(len(short)-1,-1,-1):
        if short[:i+1]==long[-i-1:]:
            return [i+1,long+short[i+1:]]
        if short[-i-1:]==long[:i+1]:
            return [i+1,short+long[i+1:]]
    return [0,long+short]

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        while len(words)>=2:
            tmp_string=""
            max_overlap=-1
            del_a=0
            del_b=0
            for i in range(len(words)-1):
                for j in range(i+1,len(words)):
                    tmp_result=overlap(words[i],words[j])
                    if max_overlap<tmp_result[0]:
                        max_overlap=tmp_result[0]
                        tmp_string=tmp_result[1]
                        del_a=i
                        del_b=j
            del words[del_b]
            del words[del_a]
            words.append(tmp_string)
            print(words)
        
        return words[0]

    