#!/usr/bin/python
import sys
import re

# Filter a board's coordinates through an affine transformation.
# Useful for realigning the second side of a 2-sided board.
# Get the coefficients from a regression in R.

# x_new = x_old*xx + y_old*xy + xi
# y_new = x_old*yx + y_old*yy + yi

xi, xx, xy, yi, yx, yy = map(float, sys.argv[1:7])

for n in sys.stdin:
  m = re.match(r'^P(.)(\d+),(\d+);$', n.rstrip())
  if m:
    c = m.group(1)
    x, y = map(float, m.groups()[1:])
    xn = xi + xx*x + xy*y
    yn = yi + yx*x + yy*y
    sys.stdout.write("P%s%4d,%4d;\n" % (c, round(xn), round(yn)))
  else:
    sys.stdout.write(n)
