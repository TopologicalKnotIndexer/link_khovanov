# link-khovanov

Compute distinct integral Khovanov homologies across component orientations of a link.

## Installation

```bash
pip install link-khovanov
```

## Usage example

```python
from link_khovanov import link_khovanov

hopf = [[2, 3, 1, 4], [4, 1, 3, 2]]
for value in link_khovanov(hopf):
    print(value)
```

## Algorithm

The PD component graph is decomposed into oriented cycles. One global orientation is fixed because reversing every component simultaneously is redundant; the remaining `2^(n-1)` orientation representatives are evaluated and duplicate homology strings are removed. Computation is delegated in batches to the Khovanov backend to avoid starting a new compiler or process for every orientation.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

- A C++14 compiler is required by the Khovanov backend on first use.
- No Java runtime is required.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
