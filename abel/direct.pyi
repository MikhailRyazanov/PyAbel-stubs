from typing import Any, Callable, Literal, Protocol
from numpy import ndarray
from .transform import Direction

cython_ext: bool = ...

def _construct_r_grid(
    n: int,
    dr: None | float = ...,
    r: None | ndarray = ...
) -> tuple[ndarray, float]: ...

class IntFunc(Protocol):
    def __call__(self, y: ndarray, x: ndarray = ..., dx: float = ...,
                 axis: int = ...) -> ndarray: ...

def direct_transform(
    fr: ndarray,
    dr: None | float = ...,
    r: None | ndarray = ...,
    direction: Direction = ...,
    derivative: Callable[[ndarray], ndarray] = ...,
    int_func: IntFunc = ...,
    correction: bool = ...,
    backend: Literal['C', 'c', 'Python', 'python'] = ...,
    **kwargs: Any
) -> ndarray: ...

def _pyabel_direct_integral(
    f: ndarray,
    r: ndarray,
    correction: Literal[0, 1],
    int_func: IntFunc = ...
) -> ndarray: ...

def is_uniform_sampling(r: ndarray) -> bool: ...
