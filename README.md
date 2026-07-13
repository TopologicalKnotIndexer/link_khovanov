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

The PD component graph is decomposed into oriented cycles. One global orientation is fixed because reversing every component simultaneously is redundant; the remaining `2^(n-1)` orientation representatives are converted to explicit crossing-sign rows. Identical rows, which occur for split components that never cross another component, are removed before the batch backend call. Duplicate homology strings are also removed from the final result. This avoids starting a native process for every orientation and avoids recomputing sign-equivalent cases.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

- A C++14 compiler is required by the Khovanov backend on first use.
- No Java runtime is required.

## Development

Python 3.10 or newer is required. Unit tests mock only the native Khovanov call while exercising real PD normalization and orientation enumeration:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.
