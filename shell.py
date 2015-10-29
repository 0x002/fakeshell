#!/usr/bin/env python

import os

def run():
    while True:
        builtin_commands = ['cd', 'exit']

        line = raw_input('> ')
        split_line = line.split()
         
        if split_line[0] in builtin_commands:
            if split_line[0] == "cd":
                if len(split_line) != 1:
                  os.chdir(split_line[1])

            elif split_line[0] == "exit":
                exit()    

        else:
            pid = os.fork()

            if not pid: 
                os.execvp(split_line[0], split_line)

            else:
                os.wait()


if __name__ == '__main__':
    run()
