#!/usr/bin/env python
import serial
import sys
import time

# Send commands from standard input to the Modela MDX-20 while avoiding
# overflowing its buffer.

# We tell the serial port to use rtscts flow control, but it doesn't seem to
# work.  So we also poll the CTS line while sending.

ser = serial.Serial('/dev/ttyUSB0', 9600, rtscts=1)

# in seconds:
delay1 = 0.1  # How long to wait between lines of the file
delay2 = 0.5  # How long to wait when polling CTS

for x in sys.stdin:
  print "sending:", x.rstrip()
  ser.write(x)
  ser.flush()
  time.sleep(delay1)
  if not ser.getCTS():
    print "waiting",
    while not ser.getCTS():
      sys.stdout.write(".")
      sys.stdout.flush()
      time.sleep(delay2)
    print "ready"

print "done"
