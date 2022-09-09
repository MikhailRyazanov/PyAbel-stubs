from typing import Any, Literal
from numpy import ndarray
from abel import __deprecated

_basis: None | ndarray
_los: None | str
_pas: None | str
_radial_step: None | int
_clip: None | int

def linbasex_transform(
    IM: ndarray,
    basis_dir: None | str = ...,
    proj_angles: list[float] = ...,
    legendre_orders: list[int] = ...,
    radial_step: int = ...,
    smoothing: float = ...,
    rcond: float = ...,
    threshold: float = ...,
    return_Beta: bool = ...,
    clip: int = ...,
    norm_range: tuple[int, int] = ...,
    direction: Literal['inverse'] = ...,
    verbose: bool = ...,
    dr: Any = ...
) -> ndarray | tuple[ndarray, ndarray, ndarray, ndarray]: ...
#!! depends on "return_Beta", but see mypy issue 5621

def linbasex_transform_full(
    IM: ndarray,
    basis_dir: None | str = ...,
    proj_angles: list[float] = ...,
    legendre_orders: list[int] = ...,
    radial_step: int = ...,
    smoothing: float = ...,
    rcond: float = ...,
    threshold: float = ...,
    clip: int = ...,
    return_Beta: __deprecated = ...,  # really deprecated, so no other types
    norm_range: tuple[int, int] = ...,
    direction: Literal['inverse'] = ...,
    verbose: bool = ...
) -> tuple[ndarray, ndarray, ndarray, ndarray]: ...

def _linbasex_transform_with_basis(
    IM: ndarray,
    Basis: ndarray,
    proj_angles: list[float] = ...,
    legendre_orders: list[int] = ...,
    radial_step: int = ...,
    rcond: float = ...,
    smoothing: float = ...,
    threshold: float = ...,
    clip: int = ...,
    norm_range: tuple[int, int] = ...
) -> tuple[ndarray, ndarray, ndarray, ndarray]: ...

def _beta_solve(
    Basis: ndarray,
    bb: ndarray,
    pol: int,
    rcond: float = ...
) -> ndarray: ...

def _Slices(
    radial: ndarray,
    Beta: ndarray,
    legendre_orders: list[int],
    smoothing: float = ...
) -> tuple[ndarray, ndarray]: ...

def int_beta(
    Beta: ndarray,
    radial_step: int = ...,
    threshold: float = ...,
    regions: None | list[tuple[int, int]] = ...
) -> __deprecated: ...

def mean_beta(
    radial: ndarray,
    Beta: ndarray,
    regions: list[tuple[int, int]]
) -> ndarray: ...

def _single_Beta_norm(
    Beta: ndarray,
    threshold: float = ...,
    norm_range: tuple[int, int] = ...
) -> ndarray: ...

def _bas(
    order: int,
    angle: float,
    COS: ndarray,
    TRI: ndarray
) -> ndarray: ...

def _bs_linbasex(
    cols: int,
    proj_angles: list[float] = ...,
    legendre_orders: list[int] = ...,
    radial_step: int = ...,
    clip: int = ...
) -> ndarray: ...

def get_bs_cached(
    cols: int,
    basis_dir: None | str = ...,
    legendre_orders: list[int] = ...,
    proj_angles: list[float] = ...,
    radial_step: int = ...,
    clip: int = ...,
    verbose: bool = ...
) -> ndarray: ...

def cache_cleanup() -> None: ...

def basis_dir_cleanup(
    basis_dir: str | None = ...
) -> None: ...
