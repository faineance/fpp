# fpp [![Travis](https://img.shields.io/travis/faineance/fpp.svg?style=flat-square)](https://travis-ci.org/faineance/fpp) [![PyPI](https://img.shields.io/pypi/dm/fpp.svg?maxAge=2592000)](https://pypi.python.org/pypi/fpp/)

## Examples ( of sorts )
```python
>>> Just(1) | (lambda x: x + 1) | (lambda x: x * 3)
<class 'fpp.Just'>(6)
>>> Nothing() | (lambda x: x + 1) | (lambda x: x * 3)
<class 'fpp.Nothing'>
```
```python
>>> Just(lambda x: x + 1) * Just(1)
<class 'fpp.Just'>(2)

>>> Nothing() * Just(1)
<class 'fpp.Nothing'>
```
```python
>>> Just(1).from_maybe('return this if nothing')
1

>>> Nothing().from_maybe('return this if nothing')
'return this if nothing'
```
```python
>>> Just(1).is_just()
True

>>> Nothing().is_nothing()
False

>>> Nothing().is_just()
False

>>> Nothing().is_nothing()
True
```
```python
def greater_then_zero(v):
    if v > 0:
        return Just(v)
    else:
        return Nothing()
>>> map_maybes(greater_then_zero, [1,2,-1,3])
[1,2,3]
```
```python
>>> Just(2).maybe(2, lambda x: x + 1)
3

>>> Nothing().maybe('default', lambda x: x + 1)
'default'
```
```python
>>> from_maybes([Just(2), Nothing(), Just(3)])
[2, 3]
```
```python
>>> Just(1) == Just(1)
True

>>> Nothing() == Just(1)
False
```

## Todo
- versions of stdlib functions which return maybes ( eg int_maybe, float_maybe)
