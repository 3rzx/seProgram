import sys
import os
import socket
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

if __name__ == "__main__":
  HOST = 'localhost'
  PORT = 9000
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST,PORT))
  s.send('pid {}'.format(os.getpid()))
  funt()
  s.close()



