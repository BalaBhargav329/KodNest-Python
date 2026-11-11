class parent:
    p1 = 1200
    p2 = 1200
class child(parent):
    p3 = 2400
c = child()
print(c.p1)
print(c.p2)
print(c.p3)