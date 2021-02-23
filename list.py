'Write a program to create a list and carry some basic operation on it'
a=['1','2',1,2,'hello','world']
print(a)
a1=a.copy()
print(a1)

a.append('a')
print(a)

a3=a.reverse()
print(a)

a[1]='b'
print(a)

print(a[2:])
print(a[-2:])

print(len(a))