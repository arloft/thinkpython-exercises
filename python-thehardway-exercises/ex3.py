print "I will not count my chickens:"
# divides 30 / 6 then adds 25
print "Hens", 25 + 30 / 6

def countRoosters():
  Roosters = 100-25*3%4
  while Roosters <= 100:
    print "Have", Roosters, "roosters, give me another rooster."
    Roosters += 1
  if Roosters > 100:
    print "Whoa!", Roosters, "is too many roosters, man!"
    Roosters -= 1
    
print "Now I will count my eggs"
print 3+2+1 - 5+4%2-1 / 4+6
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
print "What is 3 + 2?", 3+2
print "What is 5 - 7?", 5 - 7
print "Oh, that's what it's false"
print "How about some more?"
print "is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
countRoosters()