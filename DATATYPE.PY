Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
print(type(a))
<class 'int'>
a=20.5
print(type(a))
<class 'float'>
x="hello world"
print(type(x))
<class 'str'>
x=1j
print(type(x))
<class 'complex'>
b=["apple","banana","cherry"]
print(type(b))
<class 'list'>
y=("apple","banana","cherry")
print(type(y))
<class 'tuple'>
x=range(6)
print(type(x))
<class 'range'>
x={"name":"john","age":"36"}
print(type(x))
<class 'dict'>
x={"apple","banana","cherry"}
print(type(x))
<class 'set'>
>>> x=frozenset({"apple","banana","cherry"})
>>> print(type(x))
<class 'frozenset'>
>>> x=True
>>> print(type(x))
<class 'bool'>
>>> x=b"hello"
>>> print(type(x))
<class 'bytes'>
>>> x=bytearray(5)
>>> print(type(x))
<class 'bytearray'>
>>> x=memoryview(bytes(5))
>>> print(type(x))
<class 'memoryview'>
>>> x=None
>>> print(type(x))
<class 'NoneType'>
