Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
L=[1,2,3,4]
type(L)
<class 'list'>
print(L)
[1, 2, 3, 4]
L.append([9,7])
print(L)
[1, 2, 3, 4, [9, 7]]
L=[1,2,3,4]
L.insert(1,8)
print(L)
[1, 8, 2, 3, 4]
l=[1,2,3,4,8]
print(l[0])
1
print(l[-1])
8
l=[1,2,3,4]
l.extend([9,8])
print(l)
[1, 2, 3, 4, 9, 8]
l=[1,2,3,4]
del(l[0])
print(l)
[2, 3, 4]
l=[1,2,3,4]
l.pop()
4
l=[1,2,3,4]
l.reverse()
print(l)
[4, 3, 2, 1]
l=[1,2,3,4]
l2=["a","b"]
print(l+l2)
[1, 2, 3, 4, 'a', 'b']
l=[18,9,2,1]
l.sort()
print(l)
[1, 2, 9, 18]
l=[1,8,3,4]
l.sort(reverse=True)
print(l)
[8, 4, 3, 1]
print(len(l))
4
l=[1,2,3,4]
print(max(l))
4
print(min(l))
1
t=(1,2,3,4)
type(t)
<class 'tuple'>
print(t)
(1, 2, 3, 4)
print(len(l))
4
t=(1,2,3,4,3,3)
print(t.count(3))
3
t=(1,2,3,4)
t.index(2)
1
s1={1,2,3}
print(s1)
{1, 2, 3}
s2={4,5,6}
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s1={1,2,3}
s2={2,4,5}
s1.intersection(s2)
{2}
s1={1,2,3}
s2={2,3,4}
s1.difference(s2)
{1}
s1={0,1,2,3}
s.add(4)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.add(4)
NameError: name 's' is not defined. Did you mean: 's1'?
s1.add(4)
print(s1)
{0, 1, 2, 3, 4}
s1.update({4,7,8})
print(s1)
{0, 1, 2, 3, 4, 7, 8}
s1={0,1,2}
s1.clear()
print(s1)
set()
s1={0,1,2}
s1.pop()
0
s1={0,1,2}
s1.discard(0)
s1
{1, 2}
s1={0,1,2}
s2=s1.copy()
s2
{0, 1, 2}
s1={1,2,3}
s1.difference_update({3})
s1
{1, 2}
s1={0,8,9}
s1.intersection_update({8})
s1
{8}
s1={1,2,3}
s2={1,4,8,9}
s1.isdisjoin(s2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s1.isdisjoin(s2)
AttributeError: 'set' object has no attribute 'isdisjoin'. Did you mean: 'isdisjoint'?
s1.isdisjoint(s2)
False
s1={1,2,3}
s2={1,2}
s1.issuperset(s2)
True
s1={1,2,3}
s2={1,4,8,9}
s1.issubset(s2)
False
s1={1,2,3}
s2={1,4,8,9}
s1.symmetric_difference(s2)
{2, 3, 4, 8, 9}
d={"name":"ram","rno":422}
d
{'name': 'ram', 'rno': 422}
d=dict([("name",'ram'),('rno',422)])
d
{'name': 'ram', 'rno': 422}
d={1:2,3:4}
d
{1: 2, 3: 4}
d=('rno':1,"name":'abc')
SyntaxError: invalid syntax
d={'rno':1,"name":'abc'}
d.values()
dict_values([1, 'abc'])
d.keys()
dict_keys(['rno', 'name'])
d.items()
dict_items([('rno', 1), ('name', 'abc')])
d={'name':'abc','rno':111}
d.pop("name")
'abc'
d.popitem()
('rno', 111)
del(d['name'])
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    del(d['name'])
KeyError: 'name'
d={'name':'abc','rno':111}
del(d['name'])
d
{'rno': 111}
d={"name":"abc",'rno':111}
d
{'name': 'abc', 'rno': 111}
d['class']:'cse'
d
{'name': 'abc', 'rno': 111}
d['class']='cse'
d
{'name': 'abc', 'rno': 111, 'class': 'cse'}
d.get('name')
'abc'
