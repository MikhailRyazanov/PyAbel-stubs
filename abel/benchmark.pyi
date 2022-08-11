from typing import Any, Callable, Literal, Sequence, TypeVar
from numpy import ndarray
from .transform import Direction, Method
from . import dasch as Dasch
from .tools.vmi import Distributions

T = TypeVar('T')
def _ensure_list(x: type[T]) -> list[T]: ...

def _roundsf(x: float, n: int) -> float: ...

class Timent(object):
    def __init__(
        self,
        skip: int = ...,
        repeat: int = ...,
        duration: float = ...): ...
    def time(
        self,
        func: Callable,
        *args: Any,
        **kwargs: Any
    ) -> float: ...

class AbelTiming(object):
    Kind = Literal['bs', 'forward', 'inverse']
    n: list[int]
    bs: dict[str, list[float]]
    fabel: dict[str, list[float]]
    iabel: dict[str, list[float]]
    def __init__(
        self,
        n: int | list[int] = ...,
        select: Literal['all'] | Method | Sequence[Method] = ...,
        repeat: int = ...,
        t_min: float = ...,
        t_max: float = ...,
        verbose: bool = ...): ...
    def _vprint(self, *args: Any, **kwargs: Any) -> None: ...
    def _append(
        self,
        kind: Kind,
        method: Method,
        result: float
    ) -> None: ...
    def _benchmark(
        self,
        kind: Kind,
        method: Method,
        func: Callable,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
    def _skip(
        *param: tuple[Kind | list[Kind], Method | list[Method]]
    ) -> Callable[[Callable[[AbelTiming], None]],
                  Callable[[AbelTiming], None]]: ...
    def _time_basex(self) -> None: ...
    def _time_direct_C(self) -> None: ...
    def _time_direct_Python(self) -> None: ...
    def _time_hansenlaw(self) -> None: ...
    def _time_linbasex(self) -> None: ...
    def _time_onion_bordas(self) -> None: ...
    def _time_dasch(self, method: Dasch.Method) -> None: ...
    def _time_onion_peeling(self) -> None: ...
    def _time_rbasex(self) -> None: ...
    def _time_three_point(self) -> None: ...
    def _time_two_point(self) -> None: ...
    def __repr__(self) -> str: ...

class DistributionsTiming(object):
    Shape = Literal['Q', 'half', 'full']
    Weight = Literal['none', 'sin', 'array', 'sin+array']
    n: list[int]
    results: dict[str, dict[str, dict[str, tuple[float, float]]]]
    def __init__(
        self,
        n: int | list[int] = ...,
        shape: Shape = ...,
        rmax: Distributions.Rmax = ...,
        order: int = ...,
        weight: Weight | list[Weight] = ...,
        method: Literal['all'] | Distributions.Method | \
                list[Distributions.Method] = ...,
        repeat: int = ...,
        t_min: float = ...): ...
    def __repr__(self) -> str: ...

def is_symmetric(
    arr: ndarray,
    i_sym: bool = ...,
    j_sym: bool = ...
) -> ndarray: ...

def absolute_ratio_benchmark(
    analytical: Any, #?? one of the classes from analytical, initialized
    recon: ndarray,
    kind: Direction = ...
) -> ndarray: ...
