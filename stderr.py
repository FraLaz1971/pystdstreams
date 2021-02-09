import sys
 
stdout_fileno = sys.stdout
stderr_fileno = sys.stderr
 
sample_input = ['Hi', 'Hello from Python', 'exit']
 
for ip in sample_input:
    # Prints to stdout
    # Tries to add an Integer with string. Raises an exception
    try:
        stdout_fileno.write(ip + '\n')
    # Catch exceptions
    except:
        stderr_fileno.write('Exception Occurred!\n ')
        stderr_fileno.write('ip = '+ip)
    try:
        ip = ip + 100
    # Catch all exceptions
    except:
        stderr_fileno.write('Exception Occurred! ip = '+ip+'\n')
