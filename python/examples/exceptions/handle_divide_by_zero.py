import sys
import module

files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError:
        print("Cannot divide by 0 in file {}".format(filename))


# before one.txt
# 100.0
# after  one.txt
# before zero.txt
# Cannot divide by 0 in file zero.txt
# before two.txt
# FileNotFoundError: [Errno 2] No such file or directory: 'two.txt'
