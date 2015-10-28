#!/usr/bin/env python

# make shell

import os


def run():
  while True:
    builtin_commands = ['cd', 'exit']

    line = raw_input('> ')
    splitLine = line.split()
     
    pid = os.fork()

    # make the command replace the shell process
    if not pid: # child, pid = 0
      if splitLine[0] not in builtin_commands:
        os.execvp(splitLine[0], splitLine)
  
      os._exit(0)
    
    else:
      # builtins
      # cd
      if splitLine[0] == "cd":
        if len(splitLine) != 1:
          os.chdir(splitLine[1])
      
      # exit
      elif splitLine[0].startswith("exit"):
        exit()    
      
      print str(os.wait())


if __name__ == '__main__':
  run()
