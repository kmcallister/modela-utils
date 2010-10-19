#!/usr/bin/python
import serial
import sys

ser = serial.Serial('/dev/ttyUSB0', 9600, rtscts=1)

class Ui(object):
  def __init__(self):
    self.x, self.y, self.z = (1600,1600,200)
    self.m = 1
    self.move(0, 0, 0)

  def move(self, dx, dy, dz):
    self.x += self.m*dx
    self.y += self.m*dy
    self.z += 10*dz
    ser.write("""
PA;PA;!PZ%04d,%04d;VS10;!VZ10;!MC0;
P%c%04d,%04d;
!MC0;""" % (self.z, self.z, 'U' if self.z >= 0 else 'D', self.x,self.y))
    ser.flush()
    print (self.x,self.y,self.z)

  def run(self):
    while True:
      x = raw_input()
      if x == '': continue
      y = 'act_'+x[0]
      if hasattr(self, y):
        getattr(self, y)(x[1:])
      else:
        print "unknown command"

  def act_q(self):
    sys.exit(0)

  def act_h(self, d): self.move(-1, 0, 0)
  def act_t(self, d): self.move( 0, 1, 0)
  def act_n(self, d): self.move( 0,-1, 0)
  def act_s(self, d): self.move( 1, 0, 0)
  def act_r(self, d): self.move( 0, 0,-1)
  def act_l(self, d): self.move( 0, 0, 1)

  def act_m(self, m): self.m = int(m)

  def act_g(self, g):
    self.x, self.y = map(int, g.split(','))
    self.move(0,0,0)


Ui().run()
