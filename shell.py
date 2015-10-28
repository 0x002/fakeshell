#!/usr/bin/env python

# make shell

import os

while True:
  line = raw_input('> ')

  # 3. builtins
  splitLine = line.split()
   
  pid = os.fork()
  #print pid
  
  # make the command replace the shell process
  if not pid: # child, pid = 0
    # builtins

    # cd
    if splitLine[0] == "cd":
      if len(splitLine) != 1:
        os.chdir(splitLine[1])
    
    # exit
    elif splitLine[0].startswith("exit"):
      os.kill(pid, 9)
      
    else:
      os.execvp(splitLine[0], splitLine)
    
    os._exit(0)
  else:
    print str(os.wait())
