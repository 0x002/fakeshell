#!/usr/bin/env python

# make shell

import os


def run():
    while True:
        builtin_commands = ['cd', 'exit']

        line = raw_input('> ')
        split_line = line.split()
         
        if split_line[0] in builtin_commands:
            # builtins don't need to be forked
            # cd
            if split_line[0] == "cd":
                if len(split_line) != 1:
                  os.chdir(split_line[1])

            # exit
            elif split_line[0].startswith("exit"):
                exit()    

        else:
            pid = os.fork()

            # make the command replace the shell process
            if not pid: # child, pid = 0
                os.execvp(split_line[0], split_line)

            else:
                #print str(os.wait()) # see what process it is
                os.wait()


if __name__ == '__main__':
    run()
