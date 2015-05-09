name = 'rydgelee'
print (name.split('l'))
print (name.count('ry'))

if name.isalpha():
    print ('name is alpha')
    
# tuple and list
a = 1
b = 2
c = 3
d = 4
x = 5
y = 6
z = 7
stuff = [a, b, c, d]
print (stuff)
print (stuff[0:3])

stuff[0:1] = [x, y, z]
print (stuff)

for thing in stuff:
    print ('thing is', thing)
    


