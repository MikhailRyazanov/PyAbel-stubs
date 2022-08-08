from numpy import ndarray

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

#?? rename to "guess_gaussian" (+ make deprecated shim)
def guss_gaussian(x: ndarray) -> tuple[float, float, float, float]: ...

def fit_gaussian(x: ndarray) -> tuple[float, float, float, float]: ...
