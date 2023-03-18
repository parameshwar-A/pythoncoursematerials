#!/usr/bin/python3

a = "indian linux user group"
print(len(a))

b = "kanchipuram linux user group"
print(b[1:4])

c = "indian linux user group"
print(c[:5])

d = "kanchipuram linux user group"
print(d[3:])

e = "indian linux user group"
print(b[-5:-2])


f = "indian linux user group"
print(f.upper())

g = "KANCHIPURAM LINUX USER GROUP"
print(g.lower())

z = "Kanchi Linux user Group"
print(z.swapcase())

h = "   indian linux user group  "
print(h.strip())

i = "chennai python group"
print(i.replace("chennai", "kanchi"))

j = "This, is linux user group"
print(j.split(","))

k = "This is linux user group from chennai"
x = k.partition("linux")
print(x)

l = "kanchi linux user group"
y = l.startswith("kanchi")
print(y)

m = "This is chennai linux user group"
print(len(m))

