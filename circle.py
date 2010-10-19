#!/usr/bin/env python

from BeautifulSoup import BeautifulStoneSoup
import sys
'''
originally created to process a single goggles board,
this script extracts circles from an SVG file,
merges duplicate centers,
and performs a very bad approximation to optimize drilling path

if the only circles in your SVG file correspond to drill holes
then this is the script for you !

there are some magic numbers that I added to force it to work
for my board
you may need to remove these for your file
--mrule

assumes accepting a SVG file
hard coded DPI conversion factor in source
also hard coded rounding factor

y axis is flipped
1.013 scale factor is added for magic
as is a 5 mil offset for more majic
'''

DPI = float(72) #the DPI of the SVG given
CHOP = 500 #the rounding factor used to determine weather two holes are the same
MAGIC = 1.013
#OFFSET = 5
data = BeautifulStoneSoup(sys.stdin)

#needed for automatic conversion of Y axis

header = data.find(name='svg')
x= float(header['x'][:-2])
y= float(header['y'][:-2])
w= float(header['width'][:-2])
h= float(header['height'][:-2])

#convert to mills
x = int(x*1000/DPI)
y = int(y*1000/DPI)
w = int(w*1000/DPI)
H = h
h = int(h*1000/DPI)

sys.stderr.write(str((x,y,w,h)))

#now, I know that all my Y coordinates need to have H/2-(y-H/2) = H-y 
#applied to them

xs = set()
for c in data.findAll(name='circle'):
  cx = float(c["cx"])/DPI*MAGIC
  cy = (H-float(c["cy"]))/DPI*MAGIC
  #y axis flip
  #cy = h-cy
  xs.add((int(CHOP*cx),int(CHOP*cy)))

ys = sorted(list(xs))

print "PA;PA;VS2;!VZ1;!MC1;!PZ-90,50;"

for x,y in ys:
  print "PU%d,%d;" % (x*1000/CHOP,y*1000/CHOP)
  print "PD%d,%d;" % (x*1000/CHOP,y*1000/CHOP)



