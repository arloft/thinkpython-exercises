from sys import argv

# script, filename = argv
script = argv

# txt = open(filename)

# print "Here's your file %r:" % filename
# print txt.read()
# txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
# disabling the above lines changes how
# the program works. Now, I give python
# only the script's name, then the script
# itself asks me what file to use, rather
# than supplying it as an argument to
# this script.
