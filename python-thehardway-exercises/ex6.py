# -*- coding: utf-8 -*-
# used this ^ because i put an ellipsis into a text string,
# produces an error without this declaration

x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# prints False because no variable is linked to the %r following the string.
# Since there isn't a value, it returns the value as False (i think...)

print joke_evaluation % hilarious

w = "This is the left side of…"
e = "a string with a right side."

print w + e
