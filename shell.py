#!/usr/bin/env python

# make shell

import os


def run():
  while True:
    builtin_commands = ['cd', 'exit']

    line = raw_input('> ')
    splitLine = line.split()
     
    if splitLine[0] in builtin_commands:
      # builtins don't need to be forked
      # cd
      if splitLine[0] == "cd":
        if len(splitLine) != 1:
          os.chdir(splitLine[1])
      
      # exit
      elif splitLine[0].startswith("exit"):
        exit()    
    
    else:
      pid = os.fork()

      # make the command replace the shell process
      if not pid: # child, pid = 0
        os.execvp(splitLine[0], splitLine)
      
      else:
        #print str(os.wait()) # see what process it is
        os.wait()


if __name__ == '__main__':
  run()
