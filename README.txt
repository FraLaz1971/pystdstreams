# usage of standard streams in python
It's supposed to use a python3 interpreter
callable with the executable named python3 (or python3.exe on MS win).
If you have a different executable name
for python3 (such as python or python3.7 or so)
change it accordingly with the actual interpreter name.

### stdin.py
usage examples:

	echo "this is a sentence" | python3 stdin.py

	printf "these \n are different \n words" | python3 stdin.py

	seq 15 | python3 stdin.py
#
	francesco@squirrel:~/projects/python/pystdstreams$ ls | python output_redirection.py 
	0) this is to the actual  --->LICENSE                                                                             
                                                                                                                  
	1) this is to the actual  --->myfile.txt                                                                          
                                                                                                                  
	2) this is to the actual  --->output_redirection.py

	3) this is to the actual  --->README

	4) this is to the actual  --->README.md

	5) this is to the actual  --->README.txt

	6) this is to the actual  --->stderr.py

	7) this is to the actual  --->stdin.py

	8) this is to the actual  --->stdout.py

	francesco@squirrel:~/projects/python/pystdstreams$ cat myfile.txt 
	0) this is to the redirected --->LICENSE

	1) this is to the redirected --->myfile.txt

	2) this is to the redirected --->output_redirection.py

	3) this is to the redirected --->README

	4) this is to the redirected --->README.md

	5) this is to the redirected --->README.txt

	6) this is to the redirected --->stderr.py

	7) this is to the redirected --->stdin.py

	8) this is to the redirected --->stdout.py

