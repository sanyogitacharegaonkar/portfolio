l=[1,2,3,4,5]
f_set=frozenset(l)
l2=[1,2,3,6,7]
f_set2=frozenset(l2)
print(f_set)
print(f_set2)
print(type(f_set))
print(type(f_set2))
print(f_set.copy())
print(f_set.difference(f_set2))
print (f_set.intersection(f_set2))
print(f_set.isdisjoint(f_set2))
print f_set.issubset(f_set2)
print (f_set.issuperset(f_set2))
print (f_set2.symmetric_difference(f_set))
print (f_set2.union(f_set))