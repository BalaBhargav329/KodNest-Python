s1 = "hello"
print(id(s1))
print(s1)
s1 = (s1 + "world")
print(s1)
print(id(s1), s1)



s1 = "hello"
s2 = s1 + "world"
print(id(s1),s1)
print(id(s2),s2)



s1 = "Python"
s2 = "Python"
print(id(s1), s2)
print(id(s2), s2)
print(s1 == s2)
print(s1 is s2)


s1 = "Python"
print(s1)
print(s1[2])
print(s1[5])
print(s1[1:4])
print(s1[0:5])
print(s1[ : ])
print(s1[ :4])
print(s1[2: ])
print(s1[1: ])
print(s1[0::1])
print(s1[0::2])
print(s1[1:5:2])
print(s1[ : :3])
print(s1[2:3])
print(s1[2:5:2])
print(s1[ :3])
print(s1[4: ])
print(s1[ : : 4])

