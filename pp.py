import sys
import time
def funt():
  print 'Protected file content:\n'
  with open('pFile','r') as f:
    for line in f:
      print line	
  f.closed
  print '===end===\ncount down start'
  for x in range(0,100):
	print x
	time.sleep(1)

funt()
