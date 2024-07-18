#operation on list
a=["apple","mango","cherry"]
a.insert(2,"ritika")
print(a)
a[0]="hii"
print(a)
a.remove("ritika")
print(a)
a.pop(2)
print(a)
a.clear()
print(a)
b=["apple","mango","cherry"]
c=["apple","mango","cherry"]
b.extend(c)
print(b)
a.extend(b)
print(a)
d=[1,2,3]
b.extend(d)
print(b)
c=[]
c.extend(b)
print(c)
c.append("hiibeautifull")
print(c)
#o/p
['apple', 'mango', 'ritika', 'cherry']
['hii', 'mango', 'ritika', 'cherry']
['hii', 'mango', 'cherry']
['hii', 'mango']
[]
['apple', 'mango', 'cherry', 'apple', 'mango', 'cherry']
['apple', 'mango', 'cherry', 'apple', 'mango', 'cherry']
['apple', 'mango', 'cherry', 'apple', 'mango', 'cherry', 1, 2, 3]
['apple', 'mango', 'cherry', 'apple', 'mango', 'cherry', 1, 2, 3]
['apple', 'mango', 'cherry', 'apple', 'mango', 'cherry', 1, 2, 3, 'hiibeautifull']