from typing import Any, Callable, Literal, Sequence, TypeVar, Union
from numpy import ndarray
from .transform import Direction, Method as TransformMethod
from .dasch import Method as DaschMethod
from .tools.vmi import DistrRmax, DistrMethod

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

AbelTimingKind = Literal['bs', 'forward', 'inverse']

class AbelTiming(object):
    n: list[int]
    bs: dict[str, list[float]]
    fabel: dict[str, list[float]]
    iabel: dict[str, list[float]]
    def __init__(
        self,
        n: int | list[int] = ...,
        select: Literal['all'] | TransformMethod | Sequence[TransformMethod] = ...,
        repeat: int = ...,
        t_min: float = ...,
        t_max: float = ...,
        verbose: bool = ...): ...
    def _vprint(self, *args: Any, **kwargs: Any) -> None: ...
    def _append(
        self,
        kind: AbelTimingKind,
        method: TransformMethod,
        result: float
    ) -> None: ...
    def _benchmark(
        self,
        kind: AbelTimingKind,
        method: TransformMethod,
        func: Callable,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
    #?? @staticmethod ??
    def _skip(*param: tuple[AbelTimingKind | list[AbelTimingKind],
                            TransformMethod | list[TransformMethod]]
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def _time_basex(self) -> None: ...
    def _time_direct_C(self) -> None: ...
    def _time_direct_Python(self) -> None: ...
    def _time_hansenlaw(self) -> None: ...
    def _time_linbasex(self) -> None: ...
    def _time_onion_bordas(self) -> None: ...
    def _time_dasch(self, method: DaschMethod) -> None: ...
    def _time_onion_peeling(self) -> None: ...
    def _time_rbasex(self) -> None: ...
    def _time_three_point(self) -> None: ...
    def _time_two_point(self) -> None: ...
    def __repr__(self) -> str: ...

DistrWeight = Literal['none', 'sin', 'array', 'sin+array']

class DistributionsTiming(object):
    n: list[int]
    results: dict[str, dict[str, dict[str, tuple[float, float]]]]
    def __init__(
        self,
        n: int | list[int] = ...,
        shape: Literal['Q', 'half', 'full'] = ...,
        rmax: DistrRmax = ...,
        order: int = ...,
        weight: DistrWeight | list[DistrWeight] = ...,
        method: Literal['all'] | DistrMethod | list[DistrMethod] = ...,
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
