__author__ = 'Lyan'
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
point=Point(1,2)
print point.x
print point.y
print type(point.x)
print point
print type(Point)

from collections import deque
q=deque(['b','c','d'])
q.append('e')
q.appendleft('a')
print q

from collections import Counter
c='aaaaaaaaaaaadddddddddddd'
count=Counter(c)
print count
count=Counter()
for ch in 'programming':
    count[ch]=count[ch]+1

print count

