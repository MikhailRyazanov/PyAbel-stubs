from typing import Callable, Literal
from numpy import ndarray
from abel import __deprecated
from abel.tools.center import Method as Origin

Method = Literal['argmax', 'lsq']

def circularize_image(
    IM: ndarray,
    method: Method = ...,
    origin: None | tuple[float, float] | Origin = ...,
    radial_range: None | tuple[int, int] = ...,
    dr: float = ...,
    dt: float = ...,
    smooth: __deprecated = ...,  # really deprecated, so no other types
    ref_angle: None | float = ...,
    inverse: bool = ...,
    return_correction: bool = ...,
    tol: float = ...,
    center: __deprecated = ...  # really deprecated, so no other types
) -> ndarray | tuple[ndarray, ndarray, ndarray, Callable[[ndarray], ndarray]]: ...
#!! depends on "return_correction", but see mypy issue 5621

def circularize(
    IM: ndarray,
    radial_correction_function: Callable[[ndarray], ndarray],
    ref_angle: None | float = ...
) -> ndarray: ...

def _residual(
    param: ndarray,
    radial: ndarray,
    profile: ndarray,
    previous: ndarray
) -> ndarray: ...

def correction(
    polarIMTrans: ndarray,
    angles: ndarray,
    radial: ndarray,
    method: Method
) -> ndarray: ...
