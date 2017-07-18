import sys
import time
from procname import setprocname
def funt():
  with open('whiteList','r') as f:
    for line in f:
      print line	
  f.closed
  for x in range(0,100):
	print x
	time.sleep(1)

#setproctitle('usb process')
#os.path.basename(__file_
#setprocname('usb_process')
funt()
