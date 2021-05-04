N = int(input())
dic = {}
for _ in range(N):
    start, end = map(int, input().split())
    if dic.get(start):
        dic[start].append(end)  # min(dic.get(start, float('inf')), end)
    else:
        dic[start] = [end]
    
for k in dic.keys():
    dic[k].sort()
        
keys = sorted(dic.keys())
end = 0
count = 0
for key in keys:
    for e in dic[key]:
        if e < end:
            end = e
        elif key >= end:
            count += 1
            end = e

print(count)

# 해당 방법이 효율적인줄알았는데 별차이가 안났다 이유가 뭘까;
# 나긴했다 272ms -> 216ms