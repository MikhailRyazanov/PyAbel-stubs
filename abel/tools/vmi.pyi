from typing import Any, Literal, Optional, Union
from numpy import ndarray
from abel import __deprecated

def radial_intensity(
    kind: Literal['int2D', 'int3D', 'avg2D', 'avg3D'],
    IM: ndarray,
    origin:None | tuple[float, float] = ...,
    dr: float = ...,
    dt: None | float = ...,
) -> tuple[ndarray, ndarray]: ...

def angular_integration_3D(
    IM: ndarray,
    origin: None | tuple[float, float] = ...,
    dr: float = ...,
    dt: None | float = ...,
) -> tuple[ndarray, ndarray]: ...

def angular_integration_2D(
    IM: ndarray,
    origin: None | tuple[float, float] = ...,
    dr: float = ...,
    dt: None | float = ...,
) -> tuple[ndarray, ndarray]: ...

def average_radial_intensity_3D(
    IM: ndarray,
    origin: None | tuple[float, float] = ...,
    dr: float = ...,
    dt: None | float = ...,
) -> tuple[ndarray, ndarray]: ...

def average_radial_intensity_2D(
    IM: ndarray,
    origin: None | tuple[float, float] = ...,
    dr: float = ...,
    dt: None | float = ...,
) -> tuple[ndarray, ndarray]: ...

def angular_integration(
    IM: ndarray,
    origin: None | tuple[float, float] = ...,
    Jacobian: bool = ...,
    dr: float = ...,
    dt: None | float = ...,
) -> __deprecated: ...  # really deprecate

def average_radial_intensity(
    IM: ndarray,
    **kwargs: Any
) -> __deprecated: ...  # really deprecate

def radial_integration(
    IM: ndarray,
    origin: None | tuple[float, float] = ...,
    radial_ranges: None | list[tuple[int, int]] | int = ...
) -> tuple[list[tuple[float, float]],  # Beta
           list[tuple[float, float]],  # Amp
           list[float],  # radial_midpt
           list[float],  # Intensity_vs_theta
           ndarray]: ...  # theta

def anisotropy_parameter(
    theta: ndarray,
    intensity: ndarray,
    theta_ranges: None | list[tuple[float, float]] = ...
) -> tuple[tuple[float, float], tuple[float, float]]: ...

def toPES(
    radial: ndarray,
    intensity: ndarray,
    energy_cal_factor: float,
    per_energy_scaling: bool = ...,
    photon_energy: None | float = ...,
    Vrep: None | float = ...,
    zoom: float = ...
) -> tuple[ndarray, ndarray]: ...

DistrOrigin = Literal[
    'tl', 'tc', 'tr',    'top left',    'top center',    'top right',
    'ul', 'uc', 'ur',  'upper left',  'upper center',  'upper right',
    'cl', 'cc', 'cr', 'center left', 'center center', 'center right',
    'bl', 'bc', 'br', 'bottom left', 'bottom center', 'bottom right',
    'll', 'lc', 'lr',  'lower left',  'lower center',  'lower right',
    'c', 'center'
]

DistrRmax = Literal['hor', 'ver', 'HOR', 'VER',
                    'min', 'max', 'MIN', 'MAX', 'all']

DistrMethod = Literal['nearest', 'linear', 'remap']

class Distributions:
    origin: DistrOrigin | tuple[int, int] = ...
    rmax_in: DistrRmax | int = ...
    order: int = ...
    odd: bool = ...
    N: int = ...
    use_sin: bool = ...
    weights: None | ndarray = ...
    shape: None | tuple[int, int] = ...
    method: DistrMethod = ...
    ready: bool = ...
    def __init__(
        self,
        origin: DistrOrigin | tuple[int, int] = ...,
        rmax: DistrRmax | int = ...,
        order: int = ...,
        odd: bool = ...,
        use_sin: bool = ...,
        weights: None | ndarray = ...,
        method: DistrMethod = ...): ...
    def _int_nearest(
        self,
        a: None | ndarray,
        w: None | ndarray = ...
    ) -> ndarray: ...
    def _int_linear(
        self,
        wl: ndarray,
        wu: ndarray,
        a: None | ndarray = ...,
        w: None | ndarray = ...
    ) -> ndarray: ...
    def _int_remap(
        self,
        a: None | ndarray,
        w: None | ndarray = ...
    ) -> ndarray: ...
    rmax: int = ...
    Qheight: int = ...
    Qwidth: int = ...
    flip_row: slice = ...
    flip_col: slice = ...
    fold: bool = ...
    regions: list[tuple[slice, slice]] = ...  #??
    bin: ndarray = ...
    c: list[None | ndarray] = ...
    Qsin: None | ndarray = ...
    wu: None | ndarray = ...
    wl: None | ndarray = ...
    ntheta: int = ...
    grid: ndarray = ...
    C: ndarray = ...
    valid: ndarray = ...
    def _precalc(
        self,
        shape: tuple[int, int]
    ) -> None: ...
    class Results:
        r: ndarray = ...
        cn: ndarray = ...
        order: int = ...
        odd: bool = ...
        orders: list[int] = ...
        sinpowers: list[int] = ...
        valid: ndarray = ...
        def __init__(
            self,
            r: ndarray,
            cn: ndarray,
            order: int,
            odd: bool,
            valid: None | ndarray = ...
        ): ...
        def cos(self) -> ndarray: ...
        def rcos(self) -> ndarray: ...
        def cossin(self) -> ndarray: ...
        def rcossin(self) -> ndarray: ...
        def harmonics(self) -> ndarray: ...
        def rharmonics(self) -> ndarray: ...
        def Ibeta(self, window: int = ...) -> ndarray: ...
        def rIbeta(self, window: int = ...) -> ndarray: ...
    def image(
        self,
        IM: ndarray
    ) -> Results: ...
    def __call__(
        self,
        IM: ndarray
    ) -> Results: ...

def harmonics(
    IM: ndarray,
    origin: DistrOrigin | tuple[int, int] = ...,
    rmax: DistrRmax | int = ...,
    order: int = ...,
    **kwargs: Any  #?? passed to Distributions()
) -> ndarray: ...

def rharmonics(
    IM: ndarray,
    origin: DistrOrigin | tuple[int, int] = ...,
    rmax: DistrRmax | int = ...,
    order: int = ...,
    **kwargs: Any  #?? passed to Distributions()
) -> ndarray: ...

def Ibeta(
    IM: ndarray,
    origin: DistrOrigin | tuple[int, int] = ...,
    rmax: DistrRmax | int = ...,
    order: int = ...,
    window: int = ...,
    **kwargs: Any  #?? passed to Distributions()
) -> ndarray: ...

def rIbeta(
    IM: ndarray,
    origin: DistrOrigin | tuple[int, int] = ...,
    rmax: DistrRmax | int = ...,
    order: int = ...,
    window: int = ...,
    **kwargs: Any  #?? passed to Distributions()
) -> ndarray: ...