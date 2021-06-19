#대표적인 binary tree 만들기 문제
# 브루트 포스에 비해 일반적인 case에서 시간단축이 가능
# 회의실 예약문제와 비슷함!

class Node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=None
        self.right=None
    def insert(self,node):
        if node.end <= self.start:
            if not self.left:
                self.left=node
                return True
            else:
                return self.left.insert(node)
        elif node.start >= self.end:
            if not self.right:
                self.right=node
                return True
            else:
                return self.right.insert(node)
        else:
            return False

class MyCalendar:
    
    def __init__(self):
        self.root=None
        
    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root=Node(start,end)
            return True
        else:
            return self.root.insert(Node(start,end))