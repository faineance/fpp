# fpp [![Travis](https://img.shields.io/travis/faineance/fpp.svg?style=flat-square)](https://travis-ci.org/faineance/fpp) [![PyPI](https://img.shields.io/pypi/faineance/fpp.svg?style=flat-square)](https://pypi.python.org/pypi?name=fpp) [![PyPI](https://img.shields.io/pypi/faineance/fpp.svg?style=flat-square)](https://pypi.python.org/pypi?name=fpp)

## Examples ( of sorts )
```python
>>> Just(1) | (lambda x: x + 1) | (lambda x: x * 3)
<class 'fpp.Just'>(6)
>>> Nothing() | (lambda x: x + 1) | (lambda x: x * 3)
<class 'fpp.Nothing'>

>>> is_just(Nothing() | (lambda x: x +1))
False

>>> Just(lambda x: x + 1) * Just(1)
<class 'fpp.Just'>(2)

>>> Nothing() * Just(1)
<class 'fpp.Nothing'>

>>> Just(1) == Just(1)
True

>>> Nothing() == Just(1)
False
```