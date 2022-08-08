from typing import Any, Callable, Literal, Union
from numpy import ndarray
from abel import __deprecated

Method = Literal['image_center', 'com', 'convolution', 'gaussian', 'slice']

# same as .tools.symmetry.Axis
Axes = Union[None, Literal[0, 1], tuple[Literal[0], Literal[1]]]

Crop = Literal['maintain_size', 'valid_region', 'maintain_data']

Order = Literal[0, 1, 2, 3, 4, 5]  # scipy.ndimage.shift order

def find_origin(
    IM: ndarray,
    method: Method = ...,
    axes: Axes = ...,
    verbose: bool = ...,
    **kwargs: Any
) -> tuple[float, float]: ...

def center_image(
    IM: ndarray,
    method: Method | tuple[float | None, float | None] = ...,
    odd_size: bool = ...,
    square: bool = ...,
    axes: Axes = ...,
    crop: Crop = ...,
    order: Order = ...,
    verbose: bool = ...,
    center: __deprecated = ...,  # really deprecated, so no other types
    **kwargs: Any
) -> ndarray: ...

def set_center(
    data: ndarray,
    origin: tuple[float | None, float | None],
    crop: Crop = ...,
    axes: Axes = ...,
    order: Order = ...,
    verbose: bool = ...,
    center: __deprecated = ...,  # really deprecated, so no other types
) -> ndarray: ...

def find_origin_by_center_of_mass(
    IM: ndarray,
    axes: Axes = ...,
    verbose: bool = ...,
    round_output: bool = ...,
    **kwargs: Any
) -> tuple[float, float]: ...

def find_origin_by_convolution(
    IM: ndarray,
    axes: Axes = ...,
    projections: bool = ...,
    **kwargs: Any
) -> Union[  #!! depends on "projections", but see mypy issue 5621
    tuple[float, float],
    tuple[tuple[float, float], ndarray | None, ndarray | None]
]: ...

def find_origin_by_center_of_image(
    IM: ndarray,
    axes: Axes = ...,
    verbose: bool = ...,
    **kwargs: Any
) -> tuple[int, int]: ...  #?? switch to float, add "round_output"?

def find_origin_by_gaussian_fit(
    IM: ndarray,
    axes: Axes = ...,
    verbose: bool = ...,
    round_output: bool = ...,
    **kwargs: Any
) -> tuple[float, float]: ...

def axis_slices(
    IM: ndarray,
    radial_range: tuple[int, int] = ...,
    slice_width: int = ...
) -> tuple[ndarray, ndarray, ndarray, ndarray]: ...

def find_origin_by_slice(
    IM: ndarray,
    axes: Axes = ...,
    slice_width: int = ...,
    radial_range: tuple[int, int] = ...,
    axis: __deprecated = ...,  # really deprecated, so no other types
    **kwargs: Any
) -> tuple[float, float]: ...

func_method: dict[str, Callable[..., ndarray]]

# really deprecate old functions

def find_center(
    IM: ndarray,
    center: Method = ...,
    square: bool = ...,
    verbose: bool = ...,
    **kwargs: Any
) -> __deprecated: ...

def find_center_by_center_of_mass(
    IM: ndarray,
    verbose: bool = ...,
    round_output: bool = ...,
    **kwargs: Any
) -> __deprecated: ...

def find_center_by_convolution(
    IM: ndarray,
    **kwargs: Any
) -> __deprecated: ...

def find_center_by_center_of_image(
    IM: ndarray,
    verbose: bool = ...,
    **kwargs: Any
) -> __deprecated: ...

def find_center_by_gaussian_fit(
    IM: ndarray,
    verbose: bool = ...,
    round_output: bool = ...,
    **kwargs: Any
) -> __deprecated: ...

def find_image_center_by_slice(
    IM: ndarray,
    slice_width: int = ...,
    radial_range: tuple[int, int] = ...,
    axis: Axes = ...,
    **kwargs: Any
) -> __deprecated: ...
