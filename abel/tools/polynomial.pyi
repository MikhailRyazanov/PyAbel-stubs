from typing import overload, Sequence, TypeVar
from numpy import ndarray
from scipy.interpolate import BSpline, UnivariateSpline

class BasePolynomial(object):
    func: ndarray = ...
    abel: ndarray = ...
    T = TypeVar('T', bound='BasePolynomial')
    def copy(self: T) -> T: ...
    def __imul__(self: T, m: float) -> T: ...
    def __mul__(self: T, m: float) -> T: ...
    def __rmul__(self: T, m: float) -> T: ...
    def __itruediv__(self: T, m: float) -> T: ...
    def __truediv__(self: T, m: float) -> T: ...

class Polynomial(BasePolynomial):
    def __init__(
        self,
        r: ndarray,
        r_min: float,
        r_max: float,
        c: ndarray,
        r_0: float = ...,
        s: float = ...,
        reduced: bool = ...): ...

Range = tuple[float, float, ndarray]
RangeR0 = tuple[float, float, ndarray, float]
RangeR0S = tuple[float, float, ndarray, float, float]
RangeAny = Range | RangeR0 | RangeR0S

class PiecewisePolynomial(BasePolynomial):
    p: list[Polynomial] = ...
    def __init__(
        self,
        r: ndarray,
        ranges: Sequence[RangeAny]): ...

class SPolynomial(BasePolynomial):
    def __init__(
        self,
        r: ndarray,
        cos: ndarray,
        r_min: float,
        r_max: float,
        c: ndarray,
        r_0: float = ...,
        s: float = ...): ...

class PiecewiseSPolynomial(BasePolynomial):
    def __init__(
        self,
        r: ndarray,
        cos: ndarray,
        ranges: Sequence[RangeAny]): ...

def rcos(
    rows: None | ndarray = ...,
    cols: None | ndarray = ...,
    shape: None | tuple[int, int] = ...,
    origin: None | tuple[float, float] = ...
) -> tuple[ndarray, ndarray]: ...

class Angular(object):
    c: ndarray = ...
    def __init__(
        self,
        c: ndarray): ...
    T = TypeVar('T', bound='Angular')
    @classmethod
    def cos(
        cls: type[T],
        n: int
    ) -> T: ...
    @classmethod
    def sin(
        cls: type[T],
        n: int
    ) -> T: ...
    @classmethod
    def cossin(
        cls: type[T],
        m: int,
        n: int
    ) -> T: ...
    @classmethod
    def legendre(
        cls: type[T],
        c: Sequence[float]
    ) -> T: ...
    __array_ufunc__: None = ...
    def __add__(
        self,
        other: Angular
    ) -> Angular: ...
    def __sub__(
        self,
        other: Angular
    ) -> Angular: ...
    R = TypeVar('R', Range, RangeR0, RangeR0S)
    @overload  # by number or another angular
    def __mul__(
        self,
        obj: float | Angular
    ) -> Angular: ...
    @overload  # outer by ranges
    def __mul__(
        self,
        obj: Sequence[R]
    ) -> list[R]: ...
    @overload  # outer by sequence
    def __mul__(
        self,
        obj: Sequence[float]
    ) -> ndarray: ...
    __rmul__ = __mul__
    def __truediv__(
        self,
        num: float
    ) -> Angular: ...
    def __repr__(self) -> str: ...

class ApproxGaussian(object):
    norm: float = ...
    ranges: RangeR0S = ...
    def __init__(
        self,
        tol: float = ...): ...
    def scaled(
        self,
        A: float = ...,
        r_0: float = ...,
        sigma: float = ...
    ) -> RangeR0S: ...

def bspline(
    spl: tuple[Sequence[float], Sequence[float], int] | BSpline | UnivariateSpline
) -> list[RangeR0]: ...
