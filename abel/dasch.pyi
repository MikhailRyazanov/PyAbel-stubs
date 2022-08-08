from typing import Literal
from numpy import ndarray

Method = Literal['onion_peeling', 'two_point', 'three_point']

_D: None | ndarray
_method: None | Method
_source: None | Literal['cache', 'generated', 'file']

def two_point_transform(
    IM: ndarray,
    basis_dir: str | None = ...,
    dr: float = ...,
    direction: Literal['inverse'] = ...,
    verbose: bool = ...
) -> ndarray: ...

def three_point_transform(
    IM: ndarray,
    basis_dir: str | None = ...,
    dr: float = ...,
    direction: Literal['inverse'] = ...,
    verbose: bool = ...
) -> ndarray: ...

def onion_peeling_transform(
    IM: ndarray,
    basis_dir: str | None = ...,
    dr: float = ...,
    direction: Literal['inverse'] = ...,
    verbose: bool = ...
) -> ndarray: ...

def _dasch_transform(
    IM: ndarray,
    basis_dir: str | None = ...,
    dr: float = ...,
    direction: Literal['inverse'] = ...,
    method: Method = ...,
    verbose: bool = ...
) -> ndarray: ...

def dasch_transform(
    IM: ndarray,
    D: ndarray
) -> ndarray: ...

def _bs_two_point(cols: int) -> ndarray: ...
def _bs_three_point(cols: int) -> ndarray: ...
def _bs_onion_peeling(cols: int) -> ndarray: ...

def get_bs_cached(
    method: Method,
    cols: int,
    basis_dir: str | None = ...,
    verbose: bool = ...
) -> ndarray: ...

def cache_cleanup() -> None: ...

def basis_dir_cleanup(
    method: Method,
    basis_dir: str | None = ...
) -> None: ...
