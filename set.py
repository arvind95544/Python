s=set()
#print(type(s))
s=set([1,3,6,4])
#print(s)
s.add(5)
s.add(3)
s.remove(6)
s1=s.union([7,8])
print(s,s1)