#!/usr/bin/python
import sys
import re

# print information on a board

points = []

for n in sys.stdin:
  m = re.match(r'^P(.)\s*(\d+),\s*(\d+);', n.rstrip('\r\n'))
  if m:
    c = m.group(1)
    x, y = map(float, m.groups()[1:])
    points.append((x,y))
    print "P%s%4d,%4d;" % (c, round(x), round(y))
  else:
    print n

print 'found %d points'%len(points)
X,Y = zip(*points)
print 'X ranges from %d to %d'%(min(X),max(X))
print 'Y ranges from %d to %d'%(min(Y),max(Y))


