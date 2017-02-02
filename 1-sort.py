## Sorting

x = [4,1,2,3]
y = sorted(x)
print y
print x.sort()

x = sorted([-4,1,-2,3], key=abs, reverse=True)
print x
