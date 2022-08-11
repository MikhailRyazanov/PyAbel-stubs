from typing import Any, Callable, Literal, Sequence
from numpy import ndarray

class BaseAnalytical:
    n: int = ...
    r_max: float = ...
    r: ndarray = ...
    func: ndarray = ...
    abel: ndarray = ...
    mask_valid: ndarray = ...
    dr: float = ...
    def __init__(
        self,
        n: int,
        r_max: float,
        symmetric: bool = ...,
        **args: Any): ...

class StepAnalytical(BaseAnalytical):
    A0: float = ...
    def __init__(
        self,
        n: int,
        r_max: float,
        r1: float,
        r2: float,
        A0: float = ...,
        ratio_valid_step: float = ...,
        symmetric: bool = ...): ...
    def abel_step_analytical(
        self,
        r: ndarray,
        A0: float | ndarray,
        r0: float,
        r1: float
    ) -> ndarray: ...
    def sym_abel_step_1d(
        self,
        r: ndarray,
        A0: float | ndarray,
        r0: float,
        r1: float
    ) -> ndarray: ...

class Polynomial(BaseAnalytical):
    def __init__(
        self,
        n: int,
        r_max: float,
        r_1: float,
        r_2: float,
        c: ndarray,
        r_0: float = ...,
        s: float = ...,
        reduced: bool = ...,
        symmetric: bool = ...): ...

class PiecewisePolynomial(BaseAnalytical):
    def __init__(
        self,
        n: int,
        r_max: float,
        ranges: Sequence[tuple[float, float, ndarray]],
        symmetric: bool = ...): ...

class GaussianAnalytical(BaseAnalytical):
    sigma: float = ...
    A0: float = ...
    def __init__(
        self,
        n: int,
        r_max: int,
        sigma: float = ...,
        A0: float = ...,
        ratio_valid_sigma: float = ...,
        symmetric: bool = ...): ...

class TransformPair(BaseAnalytical):
    label: str = ...
    profile: Callable[[ndarray], tuple[ndarray, ndarray]] = ...
    def __init__(
        self,
        n: int,
        profile: Literal[1, 2, 3, 4, 5, 6, 7] = ...): ...

class SampleImage(BaseAnalytical):
    Name = Literal['Dribinski', 'Gaussian', 'Gerber', 'O2', 'Ominus']
    name: Name = ...
    def __init__(
        self,
        n: int = ...,
        name: Name = ...,
        sigma: None | float = ...,
        temperature: float = ...): ...
    def transform(
        self,
        tol: float = ...
    ) -> ndarray: ...
    @property
    def image(self) -> ndarray: ...
    @property
    def abel(self) -> ndarray: ...  # type: ignore[override]
