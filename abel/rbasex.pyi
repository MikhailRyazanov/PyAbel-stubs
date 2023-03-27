from typing import Literal
from numpy import ndarray
from .transform import Direction
from .tools.vmi import Distributions

Origin = Distributions.Origin | tuple[int, int]

Rmax = Distributions.Rmax | int

Reg = None | tuple[Literal['L2', 'diff', 'SVD'], float] |Literal['pos']

Out = Literal['same', 'fold', 'unfold', 'full', 'full-unique', None]

_prm: None | tuple[tuple[int, int],  # shape
                   Origin,  # origin
                   Rmax,  # rmax
                   int,  # order
                   bool]  # odd
_weights: None | ndarray
_dst: None | Distributions
_bs_prm: None | tuple[Rmax, int, bool]
_bs: None | list[ndarray]
_ibs: None | list[ndarray]
_trf: None | list[ndarray]
_tri_full: None | list[ndarray]
_tri_prm: None | list[Reg]
_tri: None | list[ndarray]

def rbasex_transform(
    IM: ndarray,
    origin: Origin = ...,
    rmax: Rmax = ...,
    order: int = ...,
    odd: bool = ...,
    weights: None | ndarray = ...,
    direction: Direction = ...,
    reg: Reg = ...,
    out: Out = ...,
    basis_dir: None | str = ...,
    verbose: bool = ...
) -> ndarray: ...

def _profiles(
    IM: ndarray,
    origin: Origin,
    rmax: Rmax,
    order: int,
    odd: bool,
    weights: None | ndarray,
    verbose: bool
) -> ndarray: ...

def _get_image_bs(
    height: int,
    width: int,
    row: int,
    verbose: bool
) -> list[ndarray]: ...

def _image(
    height: int,
    width: int,
    row: int,
    c: list[ndarray],
    verbose: bool
) -> ndarray: ...

def _bs_rbasex(
    Rmax: int,
    order: int,
    odd: bool
) -> list[ndarray]: ...

def _load_bs(
    basis_dir: None | str,
    Rmax: int,
    order: int,
    odd: bool,
    inv: bool = ...,
    verbose: bool = ...
) -> tuple[None | list[ndarray], None | list[ndarray]]: ...

def _save_bs(
    basis_dir: None | str,
    Rmax: int,
    order: int,
    odd: bool,
    bs: list[ndarray],
    tri: None | list[ndarray] = ...,
    verbose: bool = ...
) -> None: ...

def get_bs_cached(
    Rmax: int,
    order: int = ...,
    odd: bool = ...,
    direction: Direction = ...,
    reg: Reg = ...,
    valid: None | ndarray = ...,
    basis_dir: None | str = ...,
    verbose: bool = ...
) -> list[ndarray]: ...

def cache_cleanup(
    select: Literal['all'] | Direction = ...
) -> None: ...

def basis_dir_cleanup(
    basis_dir: str | None = ...
) -> None: ...
