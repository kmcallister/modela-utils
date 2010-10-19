#!/usr/bin/python
import serial
import sys

try:
  x, y, z = map(int, sys.argv[1:4])
except:
  print >>sys.stderr, "usage: %s <x mil> <y mil> <z mil>"
  sys.exit(1)

ser = serial.Serial('/dev/ttyUSB0', 9600, rtscts=1)

ser.write("""
PA;PA;!PZ0,%04d;VS10;!VZ10;!MC0;
PU%04d,%04d;
!MC0;""" % (z,x,y))
ser.flush()
