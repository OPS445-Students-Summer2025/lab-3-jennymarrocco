#!/usr/bin/env python3
'''Lab 3 Inv 2: free space checker'''
# Author ID: jlmarroc

import subprocess

def free_space():
    result = subprocess.run("df -h / | tail -1 | awk '{print $4}'",
                            shell=True,
                            capture_output=True,
                            text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
