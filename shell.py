#!/usr/bin/env python

# make shell

import os
import sys

def run():
    while True:
        builtin_commands = ['cd', 'exit']

        line = raw_input('> ')
        split_line = line.split()
        
        redirecting_output = False
        if ">" in split_line:
            redirecting_output = True
            output_file = split_line[-1] 

        if split_line[0] in builtin_commands:

            if split_line[0] == "cd":
                if len(split_line) != 1:
                  os.chdir(split_line[1])

            elif split_line[0] == "exit":
                exit()    

        else:
            pid = os.fork()


            if not pid: 

                if redirecting_output:
                    f = os.open(output_file, os.O_RDWR|os.O_CREAT)
                    split_line_trimmed = split_line[:-2]                  
                    os.dup2(f, sys.stdout.fileno())

                    os.execvp(split_line_trimmed[0], split_line_trimmed)

                else:
                    os.execvp(split_line[0], split_line)

            else:
                os.wait()
                if redirecting_output:
                    os.close(f)


if __name__ == '__main__':
    run()

