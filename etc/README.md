소수판별 최적화

https://wikidocs.net/13
파이썬 참고자료 틈틈히 볼것


number=list(map(int,re.split('[-]',s)))

여기서 map과 list는 모두 iterable한 객체라는점에서는 동일하지만
subscriptable한점에서는 다르다.
list는 subscriptable하지만 (그렇다는 것은 []를 이용한 indexing slicing이 된다)
map은 그렇지 않기 때문에 []를 이용하려면 list화 시켜줘야한다!