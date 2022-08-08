from numpy import ndarray

def load_raw(
    filename: str,
    start: int = ...,
    end: int = ...,
    height: int = ...,
    width: int = ...
) -> ndarray: ...

def save16bitPNG(
    filename: str,
    data: ndarray
) -> None: ...

def parse_matlab_basis_sets(
    path: str
) -> tuple[ndarray, ndarray]: ...
