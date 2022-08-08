from typing import Any, Literal
from numpy import ndarray
from .transform import Direction

def hansenlaw_transform(
  image: ndarray,
  dr: float = ...,
  direction: Direction = ...,
  hold_order: Literal[0, 1] = ...,
  **kwargs: Any
) -> ndarray: ...
