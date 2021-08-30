##https://medium.com/dmsfordsm/garbage-collection-in-python-777916fd3189
## GC에 대한 간단한 실험

import sys
a=1

print(id(a),a)

a=a+1

print(id(a),a)

print(sys.getrefcount(a))
b="hello"

print(sys.getrefcount(b))
c=[b]

print(sys.getrefcount(b))
