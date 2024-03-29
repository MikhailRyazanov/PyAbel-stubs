from typing import Any, Callable, Literal, Sequence
from numpy import ndarray
from abel import __deprecated
from .tools import center as Center
from .tools import symmetry as Symmetry
from .tools.vmi import Distributions

Direction = Literal['forward', 'inverse']

Method = Literal[
    'basex',
    'daun',
    'direct',
    'hansenlaw',
    'linbasex',
    'onion_bordas',
    'onion_peeling',
    'rbasex',
    'two_point',
    'three_point'
]

Origin = Literal['none'] | Center.Method | tuple[float, float]

class Transform:
    _verbose: bool = ...
    IM: ndarray = ...
    method: Method = ...
    direction: Direction = ...
    Beta: ndarray = ...
    radial: ndarray = ...
    projection: ndarray = ...
    distr: Distributions.Results = ...
    _origin: Origin = ...
    _symmetry_axis: Symmetry.Axis = ...
    _symmetrize_method: Symmetry.Method = ...
    _use_quadrants: tuple[bool, bool, bool, bool] = ...
    _transform_options: dict[str, Any] = ...
    _recast_as_float64: bool = ...
    def __init__(
        self,
        IM: ndarray,
        direction: Direction = ...,
        method: Method = ...,
        origin: Origin = ...,
        symmetry_axis: Symmetry.Axis = ...,
        use_quadrants: tuple[bool, bool, bool, bool] = ...,
        symmetrize_method: Symmetry.Method = ...,
        angular_integration: bool = ...,
        transform_options: dict[str, Any] = ...,
        center_options: dict[str, Any] = ...,
        angular_integration_options: dict[str, Any] = ...,
        recast_as_float64: bool = ...,
        verbose: bool = ...,
        center: __deprecated = ...  # really deprecated, so no other types
    ): ...
    _verboseprint: Callable[..., None] = ...
    def _verify_some_inputs(self) -> None: ...
    def _center_image(
        self,
        method: Origin,
        **center_options: dict[str, Any]
    ) -> None: ...
    def _abel_transform_image(
        self,
        **transform_options: dict[str, Any]
    ) -> None: ...
    def _abel_transform_image_full_linbasex(
        self,
        **transform_options: dict[str, Any]
    ) -> None: ...
    def _abel_transform_image_full_rbasex(
        self,
        **transform_options: dict[str, Any]
    ) -> None: ...
    transform: ndarray = ...
    def _abel_transform_image_by_quadrant(
        self,
        **transform_options: dict[str, Any]
    ) -> None: ...
    angular_integration: tuple[ndarray, ndarray] = ...
    def _integration(
        self,
        angular_integration: bool,
        transform_options: dict[str, Any],
        **angular_integration_options: dict[str, Any]
    ) -> None: ...

_basis_dir: str | None

def set_basis_dir(
    basis_dir: str | None = ...,
    make: bool = ...
) -> None: ...

def get_basis_dir(
    make: bool = ...
) -> str | None: ...

def _make_basis_dir() -> None: ...

def default_basis_dir() -> str: ...

def basis_dir_cleanup(
    basis_dir: str | None = ...,
    method: None | Method | Sequence[Method] | Literal['all'] = ...
) -> None: ...
