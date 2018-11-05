import turtle

bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygons(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygons(bob, 25, 7)
turtle.mainloop()