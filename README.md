Stub files for PyAbel
=====================

[Stub files](https://mypy.readthedocs.io/en/stable/stubs.html) with type hints
for the [PyAbel](https://github.com/PyAbel/PyAbel/) package (master branch).
The plan is to integrate them into the PyAbel repository eventually, but for
now they are provided here as is.

The Python typing system itself and
[mypy](https://mypy.readthedocs.io/en/stable/index.html) are still more
experimental than mature and don't have enough expressive power to annotate
everything properly, but nevertheless might be helpful, and I've tried to do as
much as feasible within current limitations (Python 3.10, mypy 0.971). Please
feel free to report any found issues or suggestions.

Usage
-----

The `abel` directory structure with `*.pyi` files can be copied over the PyAbel
`abel` directory structure with its `*.py` files (the easiest way) or put
separately in a place where your type-checking tools can find and recognize it.

(`mypi.ini` is the mypy configuration file, `allow` is the `stubtest` allowlist
file used for consistency testing with `python3 -m mypy.stubtest ... abel`;
`README.md` is this description file.)
