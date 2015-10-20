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
    if splitLine[0] == "cd":
      if len(splitLine) != 1:
        os.chdir(splitLine[1]) 
    else:
      os.execvp(splitLine[0], splitLine)
  else:
    os.wait()
