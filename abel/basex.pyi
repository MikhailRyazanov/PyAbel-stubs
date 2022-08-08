from typing import Literal
from numpy import ndarray
from .transform import Direction

def basex_transform(
    data: ndarray,
    sigma: float = ...,
    reg: float = ...,
    correction: bool = ...,
    basis_dir: str | None = ...,
    dr: float = ...,
    verbose: bool = ...,
    direction: Direction = ...
) -> ndarray: ...

def basex_core_transform(
    rawdata: ndarray,
    A: ndarray
) -> ndarray: ...

def _get_A(
    M: ndarray,
    Mc: ndarray,
    reg: float,
    direction: Direction
) -> ndarray: ...

def _nbf(
    n: int,
    sigma: float
) -> int: ...

_bs_prm: None | tuple[int, float]
_bs: None | tuple[ndarray, ndarray]
_trf_prm: None | tuple[float, bool, float]
_trf: None | ndarray
_tri_prm: None | tuple[float, bool, float]
_tri: None | ndarray

def get_bs_cached(
    n: int,
    sigma: float = ...,
    reg: float = ...,
    correction: bool = ...,
    basis_dir: str | None = ...,
    dr: float = ...,
    verbose: bool = ...,
    direction: Direction = ...
) -> ndarray: ...

def cache_cleanup(
  select: Direction | Literal['all'] = ...
) -> None: ...

def basis_dir_cleanup(
    basis_dir: str | None = ...
) -> None: ...

def get_basex_correction(
  A: ndarray,
  sigma: float,
  direction: Direction
) -> ndarray: ...

BASIS_SET_CUTOFF: int

def _bs_basex(
    n: int = ...,
    sigma: float = ...,
    oldM: None | ndarray = ...,
    verbose: bool = ...
) -> tuple[ndarray, ndarray]: ...
