#copy
import copy

a=[1,2,3,4,[9,8]]

b=a
c=a[:]
d=copy.copy(a)
e=copy.deepcopy(a)

print(b)
print(c)
print(d)
print(e)