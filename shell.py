#!/usr/bin/env python

# make shell

import os


def run():
    while True:
        builtin_commands = ['cd', 'exit']
        redirecting_output = False

        line = raw_input('> ')
        split_line = line.split()
        
        if ">" in split_line:
            redirecting_output = True
            output_file = split_line[-1] # get the output file
            f = open(output_file, 'w')

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
                    dup2(f, 1)

                    os.execvp(split_line_trimmed[0], split_line_trimmed)

                else:
                    os.execvp(split_line[0], split_line)

            else:
                #print str(os.wait()) # see what process it is
                os.wait()
                if redirecting_output:
                    f.close()


if __name__ == '__main__':
    run()
