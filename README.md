# fpp [![Travis](https://img.shields.io/travis/faineance/fpp.svg?style=flat-square)](https://travis-ci.org/faineance/fpp) [![PyPI](https://img.shields.io/pypi/faineance/fpp.svg?style=flat-square)](https://pypi.python.org/pypi?name=fpp) [![PyPI](https://img.shields.io/pypi/faineance/fpp.svg?style=flat-square)](https://pypi.python.org/pypi?name=fpp)

## Examples ( of sorts )
```python
>>> Just(1) | (lambda x: x + 1) | (lambda x: x * 3)
<class 'fpp.Just'>(6)
>>> Nothing() | (lambda x: x + 1) | (lambda x: x * 3)
<class 'fpp.Nothing'>

>>> Just(lambda x: x + 1) * Just(1)
<class 'fpp.Just'>(2)

>>> Nothing() * Just(1)
<class 'fpp.Nothing'>

>>> Just(1).from_maybe('return this if nothing')
1

>>> Nothing().from_maybe('return this if nothing')
'return this if nothing'

>>> Just(1).is_just()
True

>>> Nothing().is_just()
False


def greater_then_zero(v):
    if v > 0:
        return Just(v)
    else:
        return Nothing()
>>> map_maybes(greater_then_zero, [1,2,-1,3])
[<class 'fpp.Just'>(1), <class 'fpp.Just'>(2), <class 'fpp.Just'>(3)]

>>> Just(1) == Just(1)
True

>>> Nothing() == Just(1)
False

```