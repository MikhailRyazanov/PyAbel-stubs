from typing import TypeVar
from numpy import ndarray

def reproject_image_into_polar(
    data: ndarray,
    origin: None | tuple[float, float] = ...,
    Jacobian: bool = ...,
    dr: float = ...,
    dt: None | float = ...
) -> tuple[ndarray, ndarray, ndarray]: ...

def index_coords(
    data: ndarray,
    origin: None | tuple[float, float] = ...
) -> tuple[ndarray, ndarray]: ...

T = TypeVar('T', float, ndarray)

def cart2polar(
    x: T,
    y: T
) -> tuple[T, T]: ...

def polar2cart(
    r: T,
    theta: T
) -> tuple[T, T]: ...
