#!/usr/bin/env python

# make shell

import os

while True:
  line = input('> ')

  # 3. builtins
  splitLine = line.split()
   
  pid = os.fork()
  #print pid
  
  # make the command replace the shell process
  if not pid: # child
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

  else:
    os.wait()
