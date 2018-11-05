my_name = "Aaron Arlof"
my_age = 40 # sigh...
my_height = 70 # inches
my_weight = 152 # about
my_eyes = 'blue'
my_teeth = 'mostly white'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy" % my_weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# more examples to show the difference between %s (format as a string) and %r (format as the literal object)
print "This -> %r is what shows up when modulo+r is used in a string." % my_name

months = "\nJan\nFeb\nMar\nApr\nMay"
print "Here are the months (as a string): %s" % months
print "Here are the months (the literal object): %r" % months
