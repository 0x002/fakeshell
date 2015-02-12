#!/usr/bin/env python3

import os

while True:
    line = input('> ')
    os.execvp(line, [line])