from typing import Literal, Union
from numpy import ndarray

Axis = Union[None, Literal[0, 1], tuple[Literal[0], Literal[1]]]

Method = Literal['average', 'fourier']

def get_image_quadrants(
    IM: ndarray,
    reorient: bool = ...,
    symmetry_axis: Axis = ...,
    use_quadrants: tuple[bool, bool, bool, bool] = ...,
    symmetrize_method: Method = ...
) -> tuple[ndarray, ndarray, ndarray, ndarray]: ...

def put_image_quadrants(
    Q: tuple[ndarray, ndarray, ndarray, ndarray],
    original_image_shape: tuple[int, int],
    symmetry_axis: Axis = ...
) -> ndarray: ...
