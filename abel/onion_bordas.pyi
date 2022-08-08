from typing import Any, Literal
from numpy import ndarray

def _init_abel_vec(
    xc: int,
    yc: int
) -> tuple[ndarray, ndarray]: ...

def _init_abel(
    xc: int,
    yc: int
) -> tuple[ndarray, ndarray]: ...

def onion_bordas_transform(
    IM: ndarray,
    dr: float = ...,
    direction: Literal['inverse'] = ...,
    shift_grid: bool = ...,
    **kwargs: Any
) -> ndarray: ...
