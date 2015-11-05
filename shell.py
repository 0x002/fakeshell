#!/usr/bin/env python

# make shell

import os

def run():
    while True:
        builtin_commands = ['cd', 'exit']

        line = raw_input('> ')
        split_line = line.split()
        
        redirecting_output = False
        if ">" in split_line:
            redirecting_output = True
            output_file = split_line[-1] # get the output destination
            f = os.open(output_file, os.O_RDWR|os.O_CREAT)

        if split_line[0] in builtin_commands:
            # builtins don't need to be forked
            # cd
            if split_line[0] == "cd":
                if len(split_line) != 1:
                  os.chdir(split_line[1])

            # exit
            elif split_line[0] == "exit":
                exit()    

        else:
            pid = os.fork()

            # make the command replace the shell process
            if not pid: # child, pid = 0

                # if ">" in the command, only run part of the 
                # input command(ignoring last two element in 
                # arg array, > [filename])            
                if redirecting_output:
                    split_line_trimmed = split_line[:-2]
                    
                    # before executing command, redirect output 
                    # to output file
                    os.dup2(f, 1)

                    os.execvp(split_line_trimmed[0], split_line_trimmed)

                else:
                    os.execvp(split_line[0], split_line)

            else:
                #print str(os.wait()) # see what process it is
                os.wait()
                if redirecting_output:
                    os.close(f)


if __name__ == '__main__':
    run()
