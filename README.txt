# usage of standard streams in python
It's supposed to use a python3 interpreter
callable with the executable named python3 (or python3.exe on MS win).
If you have a different executable name
for python3 (such as python or python 3.7 or so)
change it accordingly with the actual interpreter name.

### stdin.py
usage examples:

	echo "this is a sentence" | python3 stdin.py

	printf "these \n are different \n words" | python3 stdin.py

	seq 15 | python3 stdin.py
