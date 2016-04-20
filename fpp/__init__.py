from abc import ABCMeta, abstractmethod


class Functor(metaclass=ABCMeta):
    @abstractmethod
    def fmap(self, func):
        return NotImplemented


class Applicative(metaclass=ABCMeta):
    @abstractmethod
    def apply(self, something):
        raise NotImplemented

    def __mul__(self, something):  # <*>
        return self.apply(something)

    @classmethod
    def pure(cls, x):
        return cls(x)


class Monad(metaclass=ABCMeta):
    @abstractmethod
    def bind(self, func):
        return NotImplemented

    @classmethod
    def unit(cls, v):
        return cls(v)

    def __or__(self, func):  # >>=
        return self.bind(func)


class Maybe(Monad, Applicative, Functor, metaclass=ABCMeta):
    @classmethod
    def empty(cls):
        return Nothing()

    def is_just(self):
        return isinstance(self, Just)

    def is_nothing(self):
        return isinstance(self, Nothing)

    def from_maybe(self, default):
        if self.is_just():
            return self._v
        else:
            return default

    def maybe(self, default, fn):
        if self.is_nothing():
            return default
        else:
            return fn(self._v)


class Nothing(Maybe):
    def fmap(self, fmapper):
        return Nothing()

    def apply(self, other):
        return Nothing()

    def append(self, other):
        return other

    def bind(self, func):
        return Nothing()

    def __eq__(self, other):
        return isinstance(other, Nothing)

    def __repr__(self):
        return "%s" % (self.__class__)


class Just(Maybe):
    def __init__(self, v):
        self._v = v

    def fmap(self, mapper):
        result = mapper(self._v)
        return Just(result)

    def apply(self, other_maybe):
        return other_maybe.fmap(self._v)

    def bind(self, func):
        return Just(func(self._v))

    def __eq__(self, other):
        return self._v == other._v

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self._v)


def from_maybes(lst):
    return [elem._v for elem in lst if elem.is_just()]


def map_maybes(fn, lst):
    # probably should clean up to avoid calculating fn(elem) twice
    return [fn(elem)._v for elem in lst if fn(elem).is_just()]
