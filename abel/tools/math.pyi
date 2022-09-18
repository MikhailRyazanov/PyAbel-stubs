from numpy import ndarray
from abel import __deprecated

def gradient(
    f: ndarray,
    x: None | ndarray = ...,
    dx: float = ...,
    axis: int = ...
) -> ndarray: ...

def gaussian(
    x: ndarray,
    a: float,
    mu: float,
    sigma: float,
    c: float
) -> ndarray: ...

def guess_gaussian(x: ndarray) -> tuple[float, float, float, float]: ...

def fit_gaussian(x: ndarray) -> tuple[float, float, float, float]: ...

# really deprecate old function
def guss_gaussian(x: ndarray) -> __deprecated: ...
