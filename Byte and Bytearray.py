'Write a program to create a byte type array and display the element'
el=[1,2,3,111,222]
x= bytes(el)
for i in x:
    print(i)

'Write a program to create a byte array and display the elements Also modify two elements'
e=[24,3,4,56,9]
a=bytearray(e)
for i in a:
    print(i,end=' ')

a[0]=1
a[1]=2
for i in a:
    print(i)