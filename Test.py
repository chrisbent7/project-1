print("heelo world..")

x = "hello"

print(x)

y=5

y=y+6

print(y)

a = "text.txt"
print(a)

b = open('text.txt', "r")
print( b.read() )


c = b.read()
print(c)

b = open('text.txt', 'r')

new = open('text2.txt', 'w')

for filewritethingy in b:
 new.write(filewritethingy.replace('my name is christopher', 'my name is chris'))
new.close()
new = open('text2.txt', 'r')
print(new.read())