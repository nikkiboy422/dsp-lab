Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
b=10.2
type(b)
<class 'float'>
a='ram'
type(a)
<class 'str'>
a=10<9
type(a)
<class 'bool'>
str='hello'
print(str)
hello
print(str[0])
h
print(str[0:3])
hel
print(str[:3])
hel
print(str[0:])
hello
a='hello'
b='world'
print(a+b)
helloworld
print(a*3)
hellohellohello
a='hello'
'a' in a
False
'o' in a
True
a.capitalize()
'Hello'
a='Hello'
a.casefold()
'hello'
a='Data science'
a.count('e')
2
a="Data science"
a.index('t')
2
a="Data science"
a.isalpha()
False
a="Datascience"
a.isalpha()
True
a='abc'
b='cde'
a.join(b)
'cabcdabce'
a='Data science'
a.partition('a')
('D', 'a', 'ta science')
a.rfind('s')
5
a='data science'
a.replace('d','b')
'bata science'
