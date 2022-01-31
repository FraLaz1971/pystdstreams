#!/usr/bin/env python
import sys

# Save the current stdout so that we can revert sys.stdout
# after we complete our redirection

stdin_fileno = sys.stdin
stdout_fileno = sys.stdout


# Redirect sys.stdout to the file
sys.stdout = open('myfile.txt', 'w')

ctr = 0
for inps in stdin_fileno:
    ctrs = str(ctr)
    # Prints to the redirected stdout ()
    sys.stdout.write(ctrs + ") this is to the redirected --->" + inps + '\n')
    # Prints to the actual saved stdout handler
    stdout_fileno.write(ctrs + ") this is to the actual  --->" + inps + '\n')
    ctr = ctr + 1

# Close the file
sys.stdout.close()
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno
