## Trie구조의 답안
## Trie구조를 이해해볼것(이미 사용예시를 봤었다)

import collections


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        _trie = lambda: collections.defaultdict(_trie)
        self.__root = _trie()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # Time: O(n)
        curr = self.__root
        for c in key:
            curr = curr[c]
        delta = val
        if "_end" in curr:
            delta -= curr["_end"]

        curr = self.__root
        for c in key:
            curr = curr[c]
            if "_count" in curr:
                curr["_count"] += delta
            else:
                curr["_count"] = delta
        curr["_end"] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # Time: O(n)
        curr = self.__root
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
        return curr["_count"]


## 다른방식의 구현
## node형식이라고봐도 좋고 dic형태를 활용한것
## 코드가 조금더 이해하긴 쉬움
class MapSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.value_map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        delta = val - self.value_map.get(key, 0)
        self.value_map[key] = val
        current = self.root
        current.update({ '_sums_': current.get('_sums_', 0) + delta })
        for character in key:
            current = current.setdefault(character, {})
            current.update({ '_sums_': current.get('_sums_', 0) + delta })

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current = self.root
        for character in prefix:
            current = current.get(character)
            if not current:
                return 0

        return current.get('_sums_', 0)