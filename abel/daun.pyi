from typing import Literal
from numpy import ndarray
from .transform import Direction

Degree = Literal[0, 1, 2, 3]

def daun_transform(
    data: ndarray,
    reg: None | float | tuple[Literal['diff', 'L2', 'L2c'], float] |
         Literal['nonneg'] = ...,
    degree: Degree = ...,
    dr: float = ...,
    direction: Direction = ...,
    basis_dir: None | str = ...,
    verbose: bool = ...
) -> ndarray: ...

RegType = Literal[None, 'diff', 'L2', 'L2c', 'nonneg']

_bs: None | ndarray
_bs_prm: None | tuple[int, Degree]
_tr: None | ndarray
_tr_prm: None | tuple[int, RegType, float]

def get_bs_cached(
    n: int,
    degree: Degree = ...,
    reg_type: RegType = ...,
    strength: float = ...,
    direction: Direction = ...,
    basis_dir: None | str = ...,
    verbose: bool = ...
) -> ndarray: ...

def _load_bs(
    basis_dir: None | str,
    n: int,
    degree: Degree,
    verbose: bool = ...
) -> ndarray | None: ...

def _save_bs(
    basis_dir: None | str,
    n: int,
    degree: Degree,
    bs: ndarray,
    verbose: bool = ...
) -> None: ...

def _bs_daun(
    n: int,
    degree: Degree = ...,
    verbose: bool = ...
) -> ndarray: ...

def cache_cleanup(
    select: Literal['all', 'inverse'] = ...
) -> None: ...

def basis_dir_cleanup(
    basis_dir: str | None = ...
) -> None: ...
