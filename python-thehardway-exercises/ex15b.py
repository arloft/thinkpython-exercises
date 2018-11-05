from sys import argv

script, filename = argv

theFile = open(filename, 'r+w')
theContents = theFile.read()

print "This is the contents of %r:" % filename, theContents

theAnswer = raw_input("Do you want to add anything to it (y/n)?")

if theAnswer == "y":
    clearTheFile = raw_input("Do you want to clear the file contents (y/n)?")
    if clearTheFile == "y":
        theFile.truncate(0)
    else:
        print "Contents preserved."
    addThisToTheFile = raw_input("> ")
    if clearTheFile == "y":
        theFile.write(addThisToTheFile)
    else:
        theFile.write("\n"+addThisToTheFile)
    theFile.seek(0)
    # ^^ send the read cursor back to a specific line,
    # in this case, line 0, so we can read the file again
    # to see the new content added
    print "Here's the whole file, with your stuff added:"
    print theFile.read()
    #theFile.close()
else:
    print "I guess we're done here."
    theFile.close()
