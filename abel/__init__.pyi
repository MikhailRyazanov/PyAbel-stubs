# import types for functions and classes imported into abel namespace
from .transform import Direction, Method, Transform as Transform
#!! from .tools.center import Method as Origin

class __deprecated:
    def __repr__(self) -> str: ...

_deprecated: __deprecated

def _deprecate(msg: str) -> None: ...
