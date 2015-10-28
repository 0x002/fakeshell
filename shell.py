#!/usr/bin/env python
  2 
  3 # make shell
  4 
  5 import os
  6 
  7 while True:
  8   line = raw_input('> ')
  9 
 10   # 3. builtins
 11   splitLine = line.split()
 12 
 13   pid = os.fork()
 14   #print pid
 15 
 16   # make the command replace the shell process
 17   if not pid: # child, pid = 0
 18     # builtins
 19 
 20     # cd
 21     if splitLine[0] == "cd":
 22       if len(splitLine) != 1:
 23         os.chdir(splitLine[1])
 24      
 25     # exit
 26     elif splitLine[0].startswith("exit"):
 27       os.kill(pid, 9)
 28       
 29     else:
 30       os.execvp(splitLine[0], splitLine)
 31   
 32     os._exit(0)
 33   else:
 34     print str(os.wait())
